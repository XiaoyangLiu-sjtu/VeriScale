import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from utils import natural_key, save_json


DEFAULT_ACCEPT_ROOT = Path("dataset") / "verinaplus"
DEFAULT_ADVERSARIAL_ROOT = Path("dataset") / "verina"
DEFAULT_OUTPUT_ROOT = Path("dataset") / "verinalite"
DEFAULT_TEST_REL = Path("test.json")
DEFAULT_MAP_REL = Path("plus") / "map_reject_outputs.json"
LITE_TEST_FILE = "test.json"
LOG_DIR_NAME = "log"
LITE_SELECTION_FILE = "accept_lite_selection.json"
MAX_LITE_TEST_CASES_PER_TASK = 50
ACCEPT_SUMMARY_FILE = "accept_adversarial_count_summary.json"


def path_for_summary(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path(__file__).resolve().parent))
    except ValueError:
        return str(path)


def stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def load_json_list(path: Path) -> List[Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Expected JSON list: {path}")
    return [row for row in data if isinstance(row, dict)]


def load_json_dict(path: Path) -> Dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return data


def input_key(input_obj: Any) -> str:
    return stable_json(input_obj)


def adversarial_func_id(adversarial_func: str) -> str:
    return hashlib.sha256(adversarial_func.encode("utf-8")).hexdigest()[:16]


def count_adversarial_funcs_by_input(map_path: Path) -> Dict[str, Dict[str, Any]]:
    counts: Dict[str, Dict[str, Any]] = {}
    for row in load_json_list(map_path):
        inp = row.get("input")
        if not isinstance(inp, dict):
            continue
        key = input_key(inp)
        if key not in counts:
            counts[key] = {
                "input": inp,
                "adversarial_funcs": set(),
                "killed_adversarial_funcs": [],
                "map_record_count": 0,
            }
        counts[key]["map_record_count"] += 1
        adversarial_func = row.get("adversarial_func")
        if isinstance(adversarial_func, str):
            if adversarial_func not in counts[key]["adversarial_funcs"]:
                counts[key]["adversarial_funcs"].add(adversarial_func)
                counts[key]["killed_adversarial_funcs"].append(
                    {
                        "adversarial_func_id": adversarial_func_id(adversarial_func),
                        "unexpected": row.get("unexpected"),
                        "adversarial_func": adversarial_func,
                    }
                )
    return counts


def build_accept_adversarial_counts(test_path: Path, map_path: Path) -> Dict[str, Any]:
    test_rows = load_json_list(test_path)
    counts_by_input = count_adversarial_funcs_by_input(map_path)

    cases = []
    for idx, row in enumerate(test_rows):
        inp = row.get("input")
        if not isinstance(inp, dict):
            continue
        count_info = counts_by_input.get(input_key(inp), {})
        adversarial_funcs: Set[str] = count_info.get("adversarial_funcs", set())
        killed_adversarial_funcs = count_info.get("killed_adversarial_funcs", [])
        cases.append(
            {
                "case_index": idx,
                "input": inp,
                "expected": row.get("expected"),
                "unexpected": row.get("unexpected"),
                "adversarial_func_count": len(adversarial_funcs),
                "map_record_count": int(count_info.get("map_record_count", 0)),
                "killed_adversarial_funcs": killed_adversarial_funcs,
            }
        )

    map_record_count = sum(info["map_record_count"] for info in counts_by_input.values())
    matched_input_keys = {input_key(row["input"]) for row in cases if row["adversarial_func_count"] > 0}
    sum_case_adversarial_func_count = sum(row["adversarial_func_count"] for row in cases)
    sum_case_map_record_count = sum(row["map_record_count"] for row in cases)
    return {
        "source_test_file": path_for_summary(test_path),
        "source_adversarial_file": path_for_summary(map_path),
        "case_count": len(cases),
        "map_input_count": len(counts_by_input),
        "map_record_count": map_record_count,
        "matched_unique_input_count": len(matched_input_keys),
        "sum_case_adversarial_func_count": sum_case_adversarial_func_count,
        "sum_case_map_record_count": sum_case_map_record_count,
        "max_adversarial_func_count": max((row["adversarial_func_count"] for row in cases), default=0),
        "cases_with_adversarial_funcs": sum(1 for row in cases if row["adversarial_func_count"] > 0),
        "cases": cases,
    }


def killed_func_ids(case: Dict[str, Any]) -> Set[str]:
    ids: Set[str] = set()
    for item in case.get("killed_adversarial_funcs", []):
        if not isinstance(item, dict):
            continue
        func_id = item.get("adversarial_func_id")
        if isinstance(func_id, str):
            ids.add(func_id)
    return ids


def killed_func_lookup(case: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    lookup: Dict[str, Dict[str, Any]] = {}
    for item in case.get("killed_adversarial_funcs", []):
        if not isinstance(item, dict):
            continue
        func_id = item.get("adversarial_func_id")
        if isinstance(func_id, str) and func_id not in lookup:
            lookup[func_id] = item
    return lookup


def select_best_set_cover_case(
    remaining_cases: List[Tuple[int, Dict[str, Any], Set[str]]],
    covered: Set[str],
) -> Optional[Tuple[int, Dict[str, Any], Set[str], Set[str]]]:
    best: Optional[Tuple[int, Dict[str, Any], Set[str], Set[str]]] = None
    best_key: Optional[Tuple[int, int, int]] = None
    for position, case, killed_ids in remaining_cases:
        newly_covered = killed_ids - covered
        if not newly_covered:
            continue
        case_index = int(case.get("case_index", position))
        key = (len(newly_covered), len(killed_ids), -case_index)
        if best_key is None or key > best_key:
            best = (position, case, killed_ids, newly_covered)
            best_key = key
    return best


def build_set_cover_from_counts(counts_data: Dict[str, Any]) -> Dict[str, Any]:
    cases = [case for case in counts_data.get("cases", []) if isinstance(case, dict)]
    case_entries = [(position, case, killed_func_ids(case)) for position, case in enumerate(cases)]
    universe: Set[str] = set()
    for _, _, killed_ids in case_entries:
        universe.update(killed_ids)

    covered: Set[str] = set()
    remaining_cases = list(case_entries)
    selected_cases = []
    selection_order = 0

    while len(covered) < len(universe):
        best = select_best_set_cover_case(remaining_cases, covered)
        if best is None:
            break

        position, case, killed_ids, newly_covered = best
        selection_order += 1
        lookup = killed_func_lookup(case)
        newly_covered_funcs = [lookup[func_id] for func_id in sorted(newly_covered) if func_id in lookup]
        selected_cases.append(
            {
                "selection_order": selection_order,
                "case_index": case.get("case_index", position),
                "input": case.get("input"),
                "expected": case.get("expected"),
                "unexpected": case.get("unexpected"),
                "adversarial_func_count": case.get("adversarial_func_count", len(killed_ids)),
                "newly_covered_adversarial_func_count": len(newly_covered),
                "newly_covered_adversarial_func_ids": sorted(newly_covered),
                "newly_covered_adversarial_funcs": newly_covered_funcs,
                "killed_adversarial_funcs": case.get("killed_adversarial_funcs", []),
            }
        )
        covered.update(newly_covered)
        remaining_cases = [entry for entry in remaining_cases if entry[0] != position]

    uncovered = universe - covered
    case_count = int(counts_data.get("case_count", len(cases)))
    return {
        "task_id": counts_data.get("task_id"),
        "source_counts_file": counts_data.get("source_counts_file"),
        "source_test_file": counts_data.get("source_test_file"),
        "source_adversarial_file": counts_data.get("source_adversarial_file"),
        "case_count": case_count,
        "candidate_case_count": len(cases),
        "selected_case_count": len(selected_cases),
        "adversarial_func_universe_count": len(universe),
        "covered_adversarial_func_count": len(covered),
        "uncovered_adversarial_func_count": len(uncovered),
        "uncovered_adversarial_func_ids": sorted(uncovered),
        "reduction_ratio": (len(selected_cases) / case_count) if case_count else 0,
        "selected_cases": selected_cases,
    }


def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def build_test_case_from_count_case(case: Dict[str, Any]) -> Dict[str, Any]:
    lite_case = {
        "input": case.get("input"),
        "expected": case.get("expected"),
    }
    if "unexpected" in case:
        lite_case["unexpected"] = case.get("unexpected")
    return lite_case


def build_lite_selection_from_set_cover(
    set_cover: Dict[str, Any],
    counts_data: Dict[str, Any],
    max_cases: int = MAX_LITE_TEST_CASES_PER_TASK,
) -> Dict[str, Any]:
    cases_by_index = {
        case.get("case_index"): case
        for case in counts_data.get("cases", [])
        if isinstance(case, dict)
    }
    set_cover_cases = [
        case for case in set_cover.get("selected_cases", [])
        if isinstance(case, dict)
    ]
    selected_indices: Set[int] = set()
    selected_metadata = []

    for selected_case in set_cover_cases:
        case_index = selected_case.get("case_index")
        index = safe_int(case_index)
        source_case = cases_by_index.get(case_index, selected_case)
        selected_indices.add(index)
        selected_metadata.append(
            {
                "case_index": index,
                "selection_reason": "set_cover",
                "selection_order": selected_case.get("selection_order"),
                "adversarial_func_count": source_case.get("adversarial_func_count", 0),
                "newly_covered_adversarial_func_count": selected_case.get("newly_covered_adversarial_func_count", 0),
                "input": source_case.get("input"),
                "expected": source_case.get("expected"),
            }
        )

    remaining_budget = max(0, max_cases - len(selected_indices))
    remaining_cases = [
        case for case in counts_data.get("cases", [])
        if isinstance(case, dict) and safe_int(case.get("case_index")) not in selected_indices
    ]
    remaining_cases = sorted(
        remaining_cases,
        key=lambda case: (
            -safe_int(case.get("adversarial_func_count")),
            -safe_int(case.get("map_record_count")),
            safe_int(case.get("case_index")),
        ),
    )

    for source_case in remaining_cases[:remaining_budget]:
        index = safe_int(source_case.get("case_index"))
        selected_indices.add(index)
        selected_metadata.append(
            {
                "case_index": index,
                "selection_reason": "supplemental_top_k",
                "adversarial_func_count": source_case.get("adversarial_func_count", 0),
                "map_record_count": source_case.get("map_record_count", 0),
                "input": source_case.get("input"),
                "expected": source_case.get("expected"),
            }
        )

    selected_metadata = sorted(selected_metadata, key=lambda case: safe_int(case.get("case_index")))
    lite_tests = [
        build_test_case_from_count_case(cases_by_index.get(case["case_index"], case))
        for case in selected_metadata
    ]
    set_cover_case_count = len({safe_int(case.get("case_index")) for case in set_cover_cases})
    return {
        "task_id": counts_data.get("task_id"),
        "max_lite_test_cases_per_task": max_cases,
        "case_count": counts_data.get("case_count", len(counts_data.get("cases", []))),
        "set_cover_case_count": set_cover_case_count,
        "supplemental_case_count": max(0, len(selected_metadata) - set_cover_case_count),
        "lite_test_case_count": len(lite_tests),
        "set_cover_exceeds_budget": set_cover_case_count > max_cases,
        "selected_cases": selected_metadata,
        "lite_tests": lite_tests,
    }


def process_task(accept_task_dir: Path, adversarial_root: Path, output_root: Path, test_rel: Path, map_rel: Path, force: bool) -> Dict[str, Any]:
    task_id = accept_task_dir.name
    test_path = accept_task_dir / test_rel
    map_path = adversarial_root / task_id / map_rel
    dst_task_dir = output_root / task_id
    dst_task_dir.mkdir(parents=True, exist_ok=True)
    log_dir = dst_task_dir / LOG_DIR_NAME
    log_dir.mkdir(parents=True, exist_ok=True)

    output_path = log_dir / "accept_adversarial_counts.json"
    set_cover_path = log_dir / "accept_set_cover.json"
    lite_test_path = dst_task_dir / LITE_TEST_FILE
    lite_selection_path = log_dir / LITE_SELECTION_FILE
    if output_path.exists() and not force:
        result = load_json_dict(output_path)
        result["skipped"] = True
    else:
        if not test_path.exists():
            raise FileNotFoundError(f"test file not found: {test_path}")
        if not map_path.exists():
            raise FileNotFoundError(f"map_reject_outputs file not found: {map_path}")

        result = build_accept_adversarial_counts(test_path, map_path)
        result["task_id"] = task_id
        result["skipped"] = False
        save_json(output_path, result)

    result["source_counts_file"] = path_for_summary(output_path)
    if set_cover_path.exists() and not force:
        set_cover = load_json_dict(set_cover_path)
    else:
        set_cover = build_set_cover_from_counts(result)
        set_cover["task_id"] = task_id
        set_cover["source_counts_file"] = path_for_summary(output_path)
        save_json(set_cover_path, set_cover)

    if force or not lite_test_path.exists() or not lite_selection_path.exists():
        lite_selection = build_lite_selection_from_set_cover(set_cover, result)
        lite_tests = lite_selection["lite_tests"]
        save_json(lite_test_path, lite_tests)
        selection_for_output = dict(lite_selection)
        selection_for_output.pop("lite_tests", None)
        selection_for_output["source_counts_file"] = path_for_summary(output_path)
        selection_for_output["source_set_cover_file"] = path_for_summary(set_cover_path)
        selection_for_output["lite_test_file"] = path_for_summary(lite_test_path)
        save_json(lite_selection_path, selection_for_output)
    else:
        lite_tests = load_json_list(lite_test_path)
        lite_selection = load_json_dict(lite_selection_path)

    result["set_cover_file"] = path_for_summary(set_cover_path)
    result["lite_test_file"] = path_for_summary(lite_test_path)
    result["lite_selection_file"] = path_for_summary(lite_selection_path)
    result["lite_test_case_count"] = len(lite_tests)
    result["lite_test_budget"] = lite_selection.get("max_lite_test_cases_per_task", MAX_LITE_TEST_CASES_PER_TASK)
    result["lite_supplemental_case_count"] = lite_selection.get("supplemental_case_count", 0)
    result["lite_set_cover_exceeds_budget"] = lite_selection.get("set_cover_exceeds_budget", False)
    result["set_cover_selected_case_count"] = set_cover.get("selected_case_count", 0)
    result["set_cover_adversarial_func_universe_count"] = set_cover.get("adversarial_func_universe_count", 0)
    result["set_cover_covered_adversarial_func_count"] = set_cover.get("covered_adversarial_func_count", 0)
    result["set_cover_uncovered_adversarial_func_count"] = set_cover.get("uncovered_adversarial_func_count", 0)
    result["set_cover_reduction_ratio"] = set_cover.get("reduction_ratio", 0)
    return result


def reduce_accept(
    accept_root: Path = DEFAULT_ACCEPT_ROOT,
    adversarial_root: Path = DEFAULT_ADVERSARIAL_ROOT,
    output_root: Path = DEFAULT_OUTPUT_ROOT,
    test_rel: Path = DEFAULT_TEST_REL,
    map_rel: Path = DEFAULT_MAP_REL,
    task_pattern: str = "verina_*",
    force: bool = False,
) -> Dict[str, Any]:
    accept_root = accept_root.resolve()
    adversarial_root = adversarial_root.resolve()
    output_root = output_root.resolve()
    task_dirs = sorted([p for p in accept_root.glob(task_pattern) if p.is_dir()], key=natural_key)
    output_root.mkdir(parents=True, exist_ok=True)

    task_summaries = []
    for task_dir in task_dirs:
        try:
            result = process_task(
                accept_task_dir=task_dir,
                adversarial_root=adversarial_root,
                output_root=output_root,
                test_rel=test_rel,
                map_rel=map_rel,
                force=force,
            )
            task_summaries.append(
                {
                    "task_id": result.get("task_id", task_dir.name),
                    "case_count": result.get("case_count", 0),
                    "map_input_count": result.get("map_input_count", 0),
                    "map_record_count": result.get("map_record_count", 0),
                    "matched_unique_input_count": result.get("matched_unique_input_count", 0),
                    "sum_case_adversarial_func_count": result.get("sum_case_adversarial_func_count", 0),
                    "sum_case_map_record_count": result.get("sum_case_map_record_count", 0),
                    "max_adversarial_func_count": result.get("max_adversarial_func_count", 0),
                    "cases_with_adversarial_funcs": result.get("cases_with_adversarial_funcs", 0),
                    "set_cover_selected_case_count": result.get("set_cover_selected_case_count", 0),
                    "set_cover_adversarial_func_universe_count": result.get("set_cover_adversarial_func_universe_count", 0),
                    "set_cover_covered_adversarial_func_count": result.get("set_cover_covered_adversarial_func_count", 0),
                    "set_cover_uncovered_adversarial_func_count": result.get("set_cover_uncovered_adversarial_func_count", 0),
                    "set_cover_reduction_ratio": result.get("set_cover_reduction_ratio", 0),
                    "set_cover_file": result.get("set_cover_file"),
                    "lite_test_file": result.get("lite_test_file"),
                    "lite_selection_file": result.get("lite_selection_file"),
                    "lite_test_budget": result.get("lite_test_budget", MAX_LITE_TEST_CASES_PER_TASK),
                    "lite_test_case_count": result.get("lite_test_case_count", 0),
                    "lite_supplemental_case_count": result.get("lite_supplemental_case_count", 0),
                    "lite_set_cover_exceeds_budget": result.get("lite_set_cover_exceeds_budget", False),
                    "skipped": result.get("skipped", False),
                }
            )
        except Exception as e:
            task_summaries.append({"task_id": task_dir.name, "error": str(e)})

    summary = {
        "accept_root": path_for_summary(accept_root),
        "adversarial_root": path_for_summary(adversarial_root),
        "output_root": path_for_summary(output_root),
        "test_rel": str(test_rel),
        "map_rel": str(map_rel),
        "task_count": len(task_summaries),
        "tasks": task_summaries,
    }
    summary_dir = output_root / LOG_DIR_NAME
    summary_dir.mkdir(parents=True, exist_ok=True)
    save_json(summary_dir / ACCEPT_SUMMARY_FILE, summary)
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Count adversarial functions per accept input from map_reject_outputs.json.")
    parser.add_argument("--accept-root", type=Path, default=DEFAULT_ACCEPT_ROOT)
    parser.add_argument("--adversarial-root", type=Path, default=DEFAULT_ADVERSARIAL_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--test-rel", type=Path, default=DEFAULT_TEST_REL)
    parser.add_argument("--map-rel", type=Path, default=DEFAULT_MAP_REL)
    parser.add_argument("--task-pattern", type=str, default="verina_*")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    summary = reduce_accept(
        accept_root=args.accept_root,
        adversarial_root=args.adversarial_root,
        output_root=args.output_root,
        test_rel=args.test_rel,
        map_rel=args.map_rel,
        task_pattern=args.task_pattern,
        force=args.force,
    )
    print(json.dumps(
        {
            "accept_root": summary["accept_root"],
            "adversarial_root": summary["adversarial_root"],
            "output_root": summary["output_root"],
            "task_count": summary["task_count"],
            "summary_file": str(Path(summary["output_root"]) / LOG_DIR_NAME / ACCEPT_SUMMARY_FILE),
        },
        ensure_ascii=False,
        indent=2,
    ))
