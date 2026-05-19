import re
import json
import random
from tqdm import tqdm
from pathlib import Path
from typing import Any, Dict, List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import save_json
from src.output.step4_accept_output import _load_task_meta, build_call_expr, run_lean_eval, parse_expected_output


_NEXT_DECL_PATTERN = re.compile(r"(?m)^(?:def|theorem|lemma|example|abbrev|opaque|axiom)\s+\w+\b")
_MAX_EVAL_CASES = 3000
_SAMPLE_SEED = 20260426


def _replace_target_def(lean_source: str, fn_name: str, replacement_def: str) -> str:
    match = re.search(rf"(?m)^def\s+{re.escape(fn_name)}\b", lean_source)
    if not match:
        raise ValueError(f"Cannot find function definition `def {fn_name}` in task lean source.")

    start = match.start()
    next_decl = _NEXT_DECL_PATTERN.search(lean_source, match.end())
    end = next_decl.start() if next_decl else len(lean_source)

    replacement = (replacement_def or "").strip()
    if not replacement:
        raise ValueError("Empty adversarial function code.")

    return lean_source[:start] + replacement + "\n\n" + lean_source[end:].lstrip("\n")


def _dedup_codes(codes: List[Any]) -> List[str]:
    seen = set()
    out: List[str] = []
    for code in codes or []:
        if not isinstance(code, str):
            continue
        c = code.strip()
        if not c or c in seen:
            continue
        seen.add(c)
        out.append(c)
    return out


def _ensure_unexpected_list(row: Dict[str, Any]) -> None:
    if "unexpected" not in row or not isinstance(row["unexpected"], list):
        row["unexpected"] = []


def _append_unexpected(row: Dict[str, Any], value: Any) -> bool:
    _ensure_unexpected_list(row)
    for old in row["unexpected"]:
        if old == value:
            return False
    row["unexpected"].append(value)
    return True


def _evaluate_one_pair(row_idx: int, adv_idx: int, row: Dict[str, Any], call_expr: str, return_type: str, lean_source: str, root_dir: Path, timeout: int) -> Dict[str, Any]:
    try:
        ok, eval_output = run_lean_eval(root_dir=root_dir, task_lean_source=lean_source, call_expr=call_expr, timeout=timeout)
        if not ok:
            raise RuntimeError(eval_output)
        value = parse_expected_output(return_type, eval_output)
        return {
            "row_idx": row_idx,
            "adv_idx": adv_idx,
            "value": value,
            "expected": row.get("expected"),
        }
    except Exception as e:
        return {
            "row_idx": row_idx,
            "adv_idx": adv_idx,
            "error": str(e),
            "input": row.get("input"),
        }


def generate_reject_outputs_from_adversarial(
    task_dir: Path,
    root_dir: Path,
    adversarial_codes: List[str],
    test_rel: str = "plus/test.json",
    map_rel: str = "plus/map_reject_outputs.json",
    timeout: int = 60,
    workers: int = 50,
) -> Dict[str, Any]:
    task_dir = task_dir.resolve()
    root_dir = root_dir.resolve()

    test_path = task_dir / test_rel
    map_path = task_dir / map_rel

    if not test_path.exists():
        raise FileNotFoundError(f"test file not found: {test_path}")

    task_meta = _load_task_meta(task_dir)
    tests = json.loads(test_path.read_text())
    if not isinstance(tests, list):
        raise ValueError(f"test file is not a JSON list: {test_path}")

    # Reset previous step5 artifacts so reruns start from a clean state.
    for row in tests:
        if isinstance(row, dict):
            row["unexpected"] = []

    adversarial_codes = _dedup_codes(adversarial_codes)
    replaced_jobs: List[Tuple[str, str]] = []
    build_errors: List[Dict[str, Any]] = []
    for adv_idx, code in enumerate(adversarial_codes):
        try:
            replaced_source = _replace_target_def(task_meta["lean_source"], task_meta["name"], code)
            replaced_jobs.append((code, replaced_source))
        except Exception as e:
            build_errors.append({"adversarial_index": adv_idx, "error": str(e)})

    workers = max(1, int(workers))
    max_eval_cases = max(0, int(_MAX_EVAL_CASES))
    job_inputs: List[Tuple[int, int, Dict[str, Any], str]] = []
    errors: List[Dict[str, Any]] = list(build_errors)

    for row_idx, row in enumerate(tests):
        if not isinstance(row, dict) or not isinstance(row.get("input"), dict):
            errors.append({"row_idx": row_idx, "error": f"Invalid test row: {row}"})
            continue
        try:
            call_expr = build_call_expr(task_meta, row["input"])
        except Exception as e:
            errors.append({"row_idx": row_idx, "input": row.get("input"), "error": str(e)})
            continue

        for adv_idx, (_adv_code, lean_source) in enumerate(replaced_jobs):
            job_inputs.append((row_idx, adv_idx, row, call_expr))

    if len(job_inputs) > max_eval_cases:
        rng = random.Random(f"{_SAMPLE_SEED}:{task_dir.name}")
        job_inputs = rng.sample(job_inputs, max_eval_cases)

    outcomes: List[Dict[str, Any]] = []
    if workers == 1:
        for row_idx, adv_idx, row, call_expr in tqdm(job_inputs, desc=f"{task_dir.name} reject eval", unit="case"):
            outcomes.append(_evaluate_one_pair(row_idx=row_idx, adv_idx=adv_idx, row=row, call_expr=call_expr, return_type=task_meta["return_type"], lean_source=replaced_jobs[adv_idx][1], root_dir=root_dir, timeout=timeout))
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [
                executor.submit(_evaluate_one_pair, row_idx, adv_idx, row, call_expr, task_meta["return_type"], replaced_jobs[adv_idx][1], root_dir, timeout)
                for row_idx, adv_idx, row, call_expr in job_inputs
            ]
            for fut in tqdm(as_completed(futures), total=len(futures), desc=f"{task_dir.name} reject eval", unit="case"):
                outcomes.append(fut.result())

    mapped_reject_outputs: List[Dict[str, Any]] = []
    for outcome in outcomes:
        if "error" in outcome:
            errors.append(outcome)
            continue

        row_idx = outcome["row_idx"]
        adv_idx = outcome["adv_idx"]
        value = outcome["value"]
        expected = outcome["expected"]
        if row_idx < 0 or row_idx >= len(tests):
            errors.append({"row_idx": row_idx, "error": "row index out of bounds"})
            continue
        if adv_idx < 0 or adv_idx >= len(replaced_jobs):
            errors.append({"row_idx": row_idx, "adv_idx": adv_idx, "error": "adversarial index out of bounds"})
            continue

        row = tests[row_idx]
        if value != expected:
            _append_unexpected(row, value)
            mapped_reject_outputs.append(
                {
                    "input": row.get("input"),
                    "expected": expected,
                    "unexpected": value,
                    "adversarial_func": replaced_jobs[adv_idx][0],
                }
            )

    for row in tests:
        if isinstance(row, dict):
            _ensure_unexpected_list(row)

    save_json(test_path, tests)
    save_json(map_path, mapped_reject_outputs)

    total_unexpected_values = 0
    for row in tests:
        if not isinstance(row, dict):
            continue
        lst = row.get("unexpected", [])
        if not isinstance(lst, list):
            continue
        if lst:
            total_unexpected_values += len(lst)

    return {
        "task_id": task_dir.name,
        "test_cases": len(tests),
        "total_unexpected_values": total_unexpected_values,
        "errors": len(errors),
        "error_details": errors[:20],
    }
