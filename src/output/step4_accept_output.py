import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import TaskDataLoader, run_lean_check, save_json


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
    buf: List[str] = []
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


def _load_task_meta(task_dir: Path) -> Dict[str, Any]:
    task_json_path = task_dir / "task.json"
    if not task_json_path.exists():
        raise FileNotFoundError(f"task.json not found: {task_json_path}")

    task_json = json.loads(task_json_path.read_text())
    signature = task_json["signature"]
    lean_rel = task_json.get("lean_file", "./task.lean")
    lean_path = (task_dir / lean_rel).resolve()
    if not lean_path.exists():
        raise FileNotFoundError(f"lean_file not found: {lean_path}")
    raw_lean = lean_path.read_text()
    lean_data = TaskDataLoader.parse_benchmark_lean_data(raw_lean, signature["name"])

    # Build a compile/eval source without proof-related sections (proof_aux/proof theorem body).
    parts: List[str] = []
    if lean_data.task_imports.strip():
        parts.append(lean_data.task_imports.strip())
    if lean_data.solution_imports.strip():
        parts.append(lean_data.solution_imports.strip())
    for block in [
        lean_data.task_aux,
        lean_data.solution_aux,
        lean_data.precond_aux,
        lean_data.precond,
        lean_data.code_aux,
        lean_data.code,
        lean_data.postcond_aux,
        lean_data.postcond,
    ]:
        if (block or "").strip():
            parts.append(block.strip())
    lean_source = "\n\n".join(parts) + "\n"

    return {
        "name": signature["name"],
        "parameters": signature.get("parameters", []),
        "return_type": signature.get("return_type", ""),
        "lean_source": lean_source,
    }


def build_call_expr(task_meta: Dict[str, Any], input_obj: Dict[str, Any]) -> str:
    fn_name = task_meta["name"]
    precond_name = f"{fn_name}_precond"
    args: List[str] = []

    for p in task_meta["parameters"]:
        p_name = p["param_name"]
        p_type = p["param_type"]
        if p_name not in input_obj:
            raise ValueError(f"Missing parameter `{p_name}` in input: {input_obj}")
        args.append(f"({render_unit_test_value(p_type, input_obj[p_name])})")

    args_str = " ".join(args)
    call_precond = f"({precond_name} {args_str})" if args_str else f"({precond_name})"
    proof = f"(by sorry)"
    call_expr = f"({fn_name} {args_str} {proof})" if args_str else f"({fn_name} {proof})"
    return call_expr


def run_lean_eval(root_dir: Path, task_lean_source: str, call_expr: str, timeout: int = 60) -> Tuple[bool, str]:
    lean_content = task_lean_source.rstrip() + "\n\n" + f"#eval! {call_expr}\n"
    ok, msg, stdout, _stderr = run_lean_check(root_dir=root_dir, lean_content=lean_content, timeout=timeout, return_raw=True)
    if not ok:
        return False, msg

    lines = [line.strip() for line in (stdout or "").splitlines() if line.strip()]
    if not lines:
        return False, "No #eval output found."

    filtered: List[str] = []
    for line in lines:
        lower = line.lower()
        if lower.startswith("warning:") or lower.startswith("note:"):
            continue
        if ".lean:" in line and ("warning:" in lower or "error:" in lower or "note:" in lower):
            continue
        filtered.append(line)

    if filtered:
        return True, filtered[-1]
    return True, lines[-1]


def parse_expected_output(return_type: str, raw_output: str) -> Any:
    text = (raw_output or "").strip()
    tokens = _split_top_level_tokens(_strip_outer_parens(_normalize_lean_type(return_type)))
    head = tokens[0] if tokens else ""

    if head in {"Int", "Nat", "UInt8"}:
        try:
            return int(text)
        except ValueError:
            return text

    if head == "Float":
        try:
            return float(text)
        except ValueError:
            return text

    if head == "Bool":
        if text == "true":
            return True
        if text == "false":
            return False
        return text

    if head == "String":
        if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                return text[1:-1]
        return text

    if head == "Char":
        if len(text) >= 2 and text[0] == "'" and text[-1] == "'":
            inner = text[1:-1]
            esc_map = {
                "\\n": "\n",
                "\\r": "\r",
                "\\t": "\t",
                "\\0": "\0",
                "\\'": "'",
                "\\\\": "\\",
            }
            return esc_map.get(inner, inner)
        return text

    return text


def _evaluate_one_case(idx: int, row: Dict[str, Any], task_meta: Dict[str, Any], root_dir: Path, timeout: int) -> Dict[str, Any]:
    if not isinstance(row, dict) or not isinstance(row.get("input"), dict):
        return {"index": idx, "error": f"Invalid row format: {row}"}

    input_obj = row["input"]
    try:
        call_expr = build_call_expr(task_meta, input_obj)
        ok, eval_output = run_lean_eval(root_dir, task_meta["lean_source"], call_expr, timeout=timeout)
        if not ok:
            raise RuntimeError(eval_output)
        expected = parse_expected_output(task_meta["return_type"], eval_output)
        return {
            "index": idx,
            "item": {
                "input": input_obj,
                "expected": expected,
            },
        }
    except Exception as e:
        return {"index": idx, "input": input_obj, "error": str(e)}


def generate_accept_outputs_from_impl(task_dir: Path, root_dir: Path, accept_inputs_rel: str = "plus/accept_inputs.json", output_rel: str = "plus/test.json", timeout: int = 60, workers: int = 50) -> Dict[str, Any]:
    task_dir = task_dir.resolve()
    root_dir = root_dir.resolve()
    accept_path = task_dir / accept_inputs_rel
    output_path = task_dir / output_rel

    if not accept_path.exists():
        raise FileNotFoundError(f"accept_inputs file not found: {accept_path}")

    task_meta = _load_task_meta(task_dir)
    accept_data = json.loads(accept_path.read_text())
    if not isinstance(accept_data, list):
        raise ValueError(f"accept_inputs is not a JSON list: {accept_path}")

    results: List[Dict[str, Any]] = []
    errors: List[Dict[str, Any]] = []
    workers = max(1, int(workers))

    if workers == 1:
        outcomes = [
            _evaluate_one_case(idx=idx, row=row, task_meta=task_meta, root_dir=root_dir, timeout=timeout)
            for idx, row in enumerate(accept_data)
        ]
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [
                executor.submit(_evaluate_one_case, idx, row, task_meta, root_dir, timeout)
                for idx, row in enumerate(accept_data)
            ]
            outcomes = [fut.result() for fut in as_completed(futures)]

    for outcome in sorted(outcomes, key=lambda x: x["index"]):
        if "item" in outcome:
            results.append(outcome["item"])
            continue
        errors.append(outcome)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    save_json(output_path, results)
    return {
        "task_id": task_dir.name,
        "accept_inputs": len(accept_data),
        "accept_outputs": len(results),
        "errors": len(errors),
        "error_details": errors[:20],
    }
