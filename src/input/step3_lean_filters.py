import re
import json
from typing import Any, Dict, List, Tuple
from concurrent.futures import ThreadPoolExecutor
from utils import TaskData, InputClassifyResult, dedup_input_wrapped, run_lean_check


DEFAULT_WORKERS = 30
DECIDABLE_ERR_MSG = "did not evaluate to `true`"
PLAUSIBLE_FAILED_MSG = "Found a counter-example!"
PLAUSIBLE_SUCCESS_MSG = "Unable to find a counter-example"
SIMP_SUCCESS_MSG = "no goals to be solved"
PLAUSIBLE_GAVE_UP_MSG = "Gave up after failing to generate values that fulfill the preconditions"
PLAUSIBLE_TEST_COMMAND = "plausible ( config := { numInst := 1000, maxSize := 100, numRetries := 20, randomSeed := some 42})"
FAST_TEST_IMPORTS = "import Plausible\n"
FALLBACK_TEST_IMPORTS = "import Plausible\nimport Mathlib\n"
MATHLIB_RETRY_HINTS = (
    "unknown constant",
    "unknown identifier",
    "unknown namespace",
    "invalid field notation",
    "failed to synthesize",
    "typeclass instance problem is stuck",
)


def _should_retry_with_mathlib(msg: str) -> bool:
    lower = (msg or "").lower()
    return any(hint in lower for hint in MATHLIB_RETRY_HINTS)


def _run_check_with_optional_mathlib(root_dir, precond_context: str, body: str) -> Tuple[bool, str]:
    fast_content = FAST_TEST_IMPORTS + "\n" + precond_context + "\n" + body
    ok, msg = run_lean_check(root_dir, fast_content)
    if ok or not _should_retry_with_mathlib(msg):
        return ok, msg

    fallback_content = FALLBACK_TEST_IMPORTS + "\n" + precond_context + "\n" + body
    fallback_ok, fallback_msg = run_lean_check(root_dir, fallback_content)
    combined_msg = (
        "[fast-imports]\n"
        + msg
        + "\n\n[fallback-imports-with-mathlib]\n"
        + fallback_msg
    )
    return fallback_ok, combined_msg


def build_precond_context(task: TaskData) -> str:
    parts = []
    if task.lean_data.task_imports:
        parts.append(task.lean_data.task_imports)
    if task.lean_data.solution_imports:
        parts.append(task.lean_data.solution_imports)
    if task.lean_data.task_aux:
        parts.append(task.lean_data.task_aux)
    solution_pre_aux = (task.lean_data.solution_aux + "\n" + task.lean_data.precond_aux).strip()
    if solution_pre_aux:
        parts.append(solution_pre_aux)
    if not task.lean_data.precond.strip():
        raise ValueError(f"Cannot extract full precondition definition from task.lean for task `{task.data_id}`")
    parts.append(task.lean_data.precond.strip())
    return "\n\n".join(parts) + "\n"


def _normalize_lean_type(lean_type: str) -> str:
    t = " ".join((lean_type or "").split())
    t = re.sub(r"^(List|Array)\s*\(\s*(.+)\s*\)$", r"\1 \2", t)
    return t


def _strip_outer_parens(text: str) -> str:
    s = text.strip()
    while s.startswith("(") and s.endswith(")"):
        depth = 0
        balanced = True
        for i, ch in enumerate(s):
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth < 0:
                    balanced = False
                    break
            if depth == 0 and i < len(s) - 1:
                balanced = False
                break
        if not balanced:
            break
        s = s[1:-1].strip()
    return s


def _split_top_level_tokens(text: str) -> List[str]:
    s = text.strip()
    tokens: List[str] = []
    buf = []
    depth = 0
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch.isspace() and depth == 0:
            if buf:
                tokens.append("".join(buf))
                buf = []
            continue
        buf.append(ch)
    if buf:
        tokens.append("".join(buf))
    return tokens


def _render_string_literal(value: Any) -> str:
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def _render_char_literal(value: Any) -> str:
    if isinstance(value, str):
        s = value.strip()
        if len(s) == 3 and s[0] == "'" and s[-1] == "'":
            ch = s[1]
        elif len(s) == 1:
            ch = s
        else:
            ch = s[0] if s else "a"
    else:
        s = str(value)
        ch = s[0] if s else "a"

    esc_map = {
        "\\": "\\\\",
        "'": "\\'",
        "\n": "\\n",
        "\r": "\\r",
        "\t": "\\t",
        "\0": "\\0",
    }
    esc = esc_map.get(ch, ch)
    return f"'{esc}'"


def _render_unknown_literal(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (list, tuple)):
        return "[" + ", ".join(_render_unknown_literal(x) for x in value) + "]"
    return str(value)


def _render_seq_literal(kind: str, elem_type: str, value: Any) -> str:
    if isinstance(value, str):
        s = value.strip()
        if kind == "List":
            if s.startswith("[") and s.endswith("]"):
                return s
            if s.startswith("#[") and s.endswith("]"):
                return s[1:]
        else:
            if s.startswith("#[") and s.endswith("]"):
                return s
            if s.startswith("[") and s.endswith("]"):
                return f"#{s}"

    if isinstance(value, (list, tuple)):
        elems = ", ".join(_render_typed_literal(elem_type, v) for v in value)
        prefix = "[" if kind == "List" else "#["
        return f"{prefix}{elems}]"

    elem = _render_typed_literal(elem_type, value)
    if kind == "List":
        return f"[{elem}]"
    return f"#[{elem}]"


def _render_prod_literal(lhs_type: str, rhs_type: str, value: Any) -> str:
    if isinstance(value, str):
        s = value.strip()
        if s.startswith("(") and s.endswith(")") and "," in s:
            return s
    if isinstance(value, (list, tuple)) and len(value) == 2:
        lhs = _render_typed_literal(lhs_type, value[0])
        rhs = _render_typed_literal(rhs_type, value[1])
        return f"({lhs}, {rhs})"
    if isinstance(value, dict) and "fst" in value and "snd" in value:
        lhs = _render_typed_literal(lhs_type, value["fst"])
        rhs = _render_typed_literal(rhs_type, value["snd"])
        return f"({lhs}, {rhs})"
    return _render_unknown_literal(value)


def _render_typed_literal(lean_type: str, value: Any) -> str:
    t = _strip_outer_parens(_normalize_lean_type(lean_type))
    tokens = _split_top_level_tokens(t)
    if not tokens:
        return _render_unknown_literal(value)

    head = tokens[0]
    if head == "Bool":
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, str) and value.strip().lower() in {"true", "false"}:
            return value.strip().lower()
        return "true" if bool(value) else "false"

    if head == "String":
        return _render_string_literal(value)
    if head == "Char":
        return _render_char_literal(value)

    if head in {"Int", "Nat", "UInt8"}:
        if isinstance(value, bool):
            return "1" if value else "0"
        if isinstance(value, int):
            return str(value)
        if isinstance(value, str):
            return value.strip()
        return str(value)

    if head == "Float":
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return str(float(value))
        return str(value).strip()

    if head in {"List", "Array"} and len(tokens) >= 2:
        elem_type = _strip_outer_parens(" ".join(tokens[1:]))
        return _render_seq_literal(head, elem_type, value)

    if head == "Prod" and len(tokens) >= 3:
        lhs_type = _strip_outer_parens(tokens[1])
        rhs_type = _strip_outer_parens(" ".join(tokens[2:]))
        return _render_prod_literal(lhs_type, rhs_type, value)

    return _render_unknown_literal(value)


def render_unit_test_value(lean_type: str, value: Any) -> str:
    return _render_typed_literal(lean_type, value)


def build_precond_call_expr(task: TaskData, input_obj: Dict[str, Any]) -> str:
    fn_name = f"{task.signature.name}_precond"
    expr = f"({fn_name}"
    for p in task.signature.parameters:
        if p.param_name not in input_obj:
            raise ValueError(f"Missing parameter `{p.param_name}`")
        expr += f" ({render_unit_test_value(p.param_type, input_obj[p.param_name])})"
    expr += ")"
    return expr


def _run_decide(root_dir, precond_context: str, expr: str, *, negate: bool,) -> Tuple[str, str]:
    target_expr = f"(¬ {expr})" if negate else expr
    body = f"#guard decide {target_expr}\n"
    ok, msg = _run_check_with_optional_mathlib(root_dir, precond_context, body)
    if ok:
        return "proved_true", msg
    if DECIDABLE_ERR_MSG in msg:
        return "proved_false", msg
    return "unknown", msg


def _run_plausible(root_dir, task: TaskData, precond_context: str, expr: str, *, negate: bool) -> Tuple[str, str]:
    precond_name = f"{task.signature.name}_precond"
    target_expr = f"(¬ {expr})" if negate else expr

    theorem = f"example : {target_expr} := by\n"
    theorem += f"  unfold {precond_name}\n"
    theorem += "  simp_all! (config := { failIfUnchanged := false })\n"
    theorem += f"  {PLAUSIBLE_TEST_COMMAND}\n"

    ok, msg = _run_check_with_optional_mathlib(root_dir, precond_context, theorem)

    if PLAUSIBLE_FAILED_MSG in msg:
        return "counterexample", msg
    if (
        PLAUSIBLE_SUCCESS_MSG in msg
        or SIMP_SUCCESS_MSG in msg
        or PLAUSIBLE_GAVE_UP_MSG in msg
        or ok
    ):
        return "no_counterexample", msg
    return "unknown", msg


def _syntax_check_one(root_dir, task: TaskData, precond_context: str, cand: Dict[str, Dict[str, Any]]) -> bool:
    inp = cand.get("input", {})
    if not isinstance(inp, dict):
        return False

    try:
        expr = build_precond_call_expr(task, inp)
    except Exception:
        return False

    body = f"#check {expr}\n"
    ok, _ = _run_check_with_optional_mathlib(root_dir, precond_context, body)
    return ok


def filter_by_syntax(root_dir, task: TaskData, candidates: List[Dict[str, Dict[str, Any]]], workers: int = DEFAULT_WORKERS) -> Tuple[List[Dict[str, Dict[str, Any]]], List[Dict[str, Dict[str, Any]]]]:
    precond_context = build_precond_context(task)
    syntax_ok = []
    syntax_error = []
    workers = max(1, int(workers))

    if workers == 1:
        decisions = [_syntax_check_one(root_dir, task, precond_context, cand) for cand in candidates]
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            decisions = list(executor.map(
                lambda c: _syntax_check_one(root_dir, task, precond_context, c),
                candidates,
            ))

    for cand, ok in zip(candidates, decisions):
        if ok:
            syntax_ok.append(cand)
        else:
            syntax_error.append(cand)

    return dedup_input_wrapped(syntax_ok), dedup_input_wrapped(syntax_error)


def classify_input_by_precond(root_dir, task: TaskData, precond_context: str, input_obj: Dict[str, Any]) -> InputClassifyResult:
    try:
        expr = build_precond_call_expr(task, input_obj)
    except Exception as e:
        return InputClassifyResult(status="syntax_error", syntax_ok=False, message=str(e))

    # Stage 1: bidirectional decide
    decide_expr_status, decide_expr_msg = _run_decide(root_dir, precond_context, expr, negate=False)
    decide_not_expr_status, decide_not_expr_msg = _run_decide(root_dir, precond_context, expr, negate=True)
    decide_trace = (f"decide(expr)={decide_expr_status}; decide(not_expr)={decide_not_expr_status}")

    decide_accept = (decide_expr_status == "proved_true" or decide_not_expr_status == "proved_false")
    decide_reject = (decide_not_expr_status == "proved_true" or decide_expr_status == "proved_false")

    if decide_accept and not decide_reject:
        return InputClassifyResult(
            status="accept",
            syntax_ok=True,
            message=decide_trace + "\n" + decide_expr_msg + "\n" + decide_not_expr_msg,
        )
    if decide_reject and not decide_accept:
        return InputClassifyResult(
            status="reject",
            syntax_ok=True,
            message=decide_trace + "\n" + decide_expr_msg + "\n" + decide_not_expr_msg,
        )
    if decide_accept and decide_reject:
        return InputClassifyResult(
            status="unknown",
            syntax_ok=True,
            message="conflict in decide; " + decide_trace,
        )

    # Stage 2: bidirectional plausible for decide-undecidable cases
    plausible_expr_status, plausible_expr_msg = _run_plausible(root_dir, task, precond_context, expr, negate=False)
    plausible_not_expr_status, plausible_not_expr_msg = _run_plausible(root_dir, task, precond_context, expr, negate=True)
    plausible_trace = (f"plausible(expr)={plausible_expr_status}; plausible(not_expr)={plausible_not_expr_status}")

    plausible_accept = plausible_not_expr_status == "counterexample"
    plausible_reject = plausible_expr_status == "counterexample"

    if plausible_accept and not plausible_reject:
        return InputClassifyResult(
            status="accept",
            syntax_ok=True,
            message=decide_trace + "\n" + plausible_trace,
        )
    if plausible_reject and not plausible_accept:
        return InputClassifyResult(
            status="reject",
            syntax_ok=True,
            message=decide_trace + "\n" + plausible_trace,
        )

    return InputClassifyResult(
        status="unknown",
        syntax_ok=True,
        message=(
            decide_trace
            + "\n"
            + plausible_trace
            + "\n"
            + plausible_expr_msg
            + "\n"
            + plausible_not_expr_msg
        ),
    )


def _classify_one(root_dir, task: TaskData, precond_context: str, cand: Dict[str, Dict[str, Any]]) -> str:
    inp = cand.get("input", {})
    if not isinstance(inp, dict):
        return "unknown"
    return classify_input_by_precond(root_dir, task, precond_context, inp).status


def filter_by_precond(root_dir, task: TaskData, syntax_ok_candidates: List[Dict[str, Dict[str, Any]]], workers: int = DEFAULT_WORKERS) -> Tuple[
    List[Dict[str, Dict[str, Any]]],
    List[Dict[str, Dict[str, Any]]],
    List[Dict[str, Dict[str, Any]]],
]:
    precond_context = build_precond_context(task)
    accept = []
    reject = []
    unknown = []
    workers = max(1, int(workers))

    if workers == 1:
        statuses = [_classify_one(root_dir, task, precond_context, cand) for cand in syntax_ok_candidates]
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            statuses = list(executor.map(
                lambda c: _classify_one(root_dir, task, precond_context, c),
                syntax_ok_candidates,
            ))

    for cand, status in zip(syntax_ok_candidates, statuses):
        if status == "accept":
            accept.append(cand)
        elif status == "reject":
            reject.append(cand)
        else:
            unknown.append(cand)

    return (
        dedup_input_wrapped(accept),
        dedup_input_wrapped(reject),
        dedup_input_wrapped(unknown),
    )
