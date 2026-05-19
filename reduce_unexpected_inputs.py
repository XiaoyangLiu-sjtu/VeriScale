import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from utils import natural_key, save_json


DEFAULT_SOURCE_ROOT = Path("dataset") / "verina"
DEFAULT_OUTPUT_ROOT = Path("dataset") / "verinalite"
DEFAULT_REJECT_INPUT_REL = Path("plus") / "reject_inputs.json"
LITE_REJECT_INPUT_FILE = "reject_inputs.json"
LOG_DIR_NAME = "log"
REJECT_INPUT_SUMMARY_FILE = "reject_input_reduction_summary.json"
KEEP_REJECT_INPUTS_PER_TASK = 50
KEEP_PER_CRITICAL_BUCKET = 1

INDEX_LIKE_PARAM_NAMES = {
    "i",
    "j",
    "k",
    "idx",
    "index",
    "pos",
    "position",
    "left",
    "right",
    "start",
    "end",
}

CRITICAL_BUCKET_ORDER = {
    "empty_seq": 0,
    "seq_lengths_mismatch": 1,
    "index_negative": 2,
    "index_zero": 3,
    "scalar_negative": 4,
    "scalar_zero": 5,
    "seq_contains_zero": 6,
    "seq_contains_negative": 7,
    "seq_has_duplicate": 8,
    "seq_unsorted": 9,
    "singleton_seq": 10,
}


def stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def length_bucket(length: Optional[int]) -> str:
    if length is None:
        return "len=NA"
    if length <= 3:
        return f"len={length}"
    if length <= 5:
        return "len=4-5"
    if length <= 10:
        return "len=6-10"
    return "len=>10"


def parse_sequence_literal(value: Any) -> Optional[List[Any]]:
    if isinstance(value, list):
        return value
    if not isinstance(value, str):
        return None

    text = value.strip()
    if text.startswith("#[") and text.endswith("]"):
        body = text[2:-1].strip()
    elif text.startswith("[") and text.endswith("]"):
        body = text[1:-1].strip()
    else:
        return None

    if not body:
        return []
    return [part.strip() for part in body.split(",")]


def parse_numeric(value: Any) -> Optional[int]:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and re.fullmatch(r"[+-]?\d+", value.strip()):
        return int(value.strip())
    return None


def parse_numeric_sequence(value: Any) -> Optional[List[int]]:
    seq = parse_sequence_literal(value)
    if seq is None:
        return None

    nums: List[int] = []
    for item in seq:
        num = parse_numeric(item)
        if num is None:
            return None
        nums.append(num)
    return nums


def value_kind_and_length(value: Any) -> Tuple[str, Optional[int]]:
    if isinstance(value, bool):
        return "bool", None
    if parse_numeric(value) is not None:
        return "scalar:int", None
    nums = parse_numeric_sequence(value)
    if nums is not None:
        return "seq:int", len(nums)
    seq = parse_sequence_literal(value)
    if seq is not None:
        return "seq:mixed", len(seq)
    if isinstance(value, str):
        return "string", len(value)
    return "unknown", None


def shape_of_value(value: Any) -> str:
    kind, length = value_kind_and_length(value)
    return f"{kind}:{length_bucket(length)}"


def collect_numbers(value: Any) -> List[int]:
    num = parse_numeric(value)
    if num is not None:
        return [num]
    nums = parse_numeric_sequence(value)
    if nums is not None:
        return nums
    if isinstance(value, dict):
        out: List[int] = []
        for item in value.values():
            out.extend(collect_numbers(item))
        return out
    if isinstance(value, list):
        out = []
        for item in value:
            out.extend(collect_numbers(item))
        return out
    return []


def input_shape(input_obj: Any) -> str:
    if not isinstance(input_obj, dict):
        return shape_of_value(input_obj)
    parts = [f"{name}={shape_of_value(input_obj[name])}" for name in sorted(input_obj)]
    return "|".join(parts)


def input_features(input_obj: Any) -> Tuple[str, ...]:
    features = set()
    if not isinstance(input_obj, dict):
        input_obj = {"input": input_obj}

    seq_lengths: List[int] = []
    for name, value in input_obj.items():
        nums = parse_numeric_sequence(value)
        if nums is not None:
            seq_lengths.append(len(nums))
            if len(nums) == 0:
                features.add(f"{name}:empty_seq")
            if len(nums) == 1:
                features.add(f"{name}:singleton_seq")
            if len(nums) > 1 and len(set(nums)) < len(nums):
                features.add(f"{name}:has_duplicate")
            if nums and len(set(nums)) == 1:
                features.add(f"{name}:all_same")
            if len(nums) > 1 and nums == sorted(nums):
                features.add(f"{name}:sorted_asc")
            if len(nums) > 1 and nums == sorted(nums, reverse=True):
                features.add(f"{name}:sorted_desc")

        numbers = collect_numbers(value)
        if 0 in numbers:
            features.add("has_zero")
        if 1 in numbers:
            features.add("has_one")
        if -1 in numbers:
            features.add("has_minus_one")
        if any(n < 0 for n in numbers):
            features.add("has_negative")
        if any(abs(n) >= 10**6 for n in numbers):
            features.add("has_large_abs")

    if len(seq_lengths) >= 2:
        if len(set(seq_lengths)) == 1:
            features.add("seq_lengths_match")
        else:
            features.add("seq_lengths_mismatch")

    return tuple(sorted(features))


def path_for_summary(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path(__file__).resolve().parent))
    except ValueError:
        return str(path)


def load_json_list(path: Path) -> List[Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Expected JSON list: {path}")
    return [row for row in data if isinstance(row, dict) and isinstance(row.get("input"), dict)]


def reject_input_key(row: Dict[str, Any]) -> str:
    return stable_json(row.get("input"))


def is_index_like(name: str) -> bool:
    lower = name.lower()
    return lower in INDEX_LIKE_PARAM_NAMES or lower.endswith("idx") or lower.endswith("index")


def critical_buckets(input_obj: Dict[str, Any]) -> Tuple[str, ...]:
    buckets = set()
    seq_lengths: List[int] = []

    for name, value in input_obj.items():
        nums = parse_numeric_sequence(value)
        scalar = parse_numeric(value)

        if nums is not None:
            seq_lengths.append(len(nums))
            if len(nums) == 0:
                buckets.add(f"empty_seq:{name}")
            if len(nums) == 1:
                buckets.add(f"singleton_seq:{name}")
            if 0 in nums:
                buckets.add(f"seq_contains_zero:{name}")
            if any(n < 0 for n in nums):
                buckets.add(f"seq_contains_negative:{name}")
            if len(nums) > 1 and len(set(nums)) < len(nums):
                buckets.add(f"seq_has_duplicate:{name}")
            if len(nums) > 1 and nums != sorted(nums):
                buckets.add(f"seq_unsorted:{name}")

        if scalar is not None:
            if scalar < 0:
                bucket = "index_negative" if is_index_like(name) else "scalar_negative"
                buckets.add(f"{bucket}:{name}")
            if scalar == 0:
                bucket = "index_zero" if is_index_like(name) else "scalar_zero"
                buckets.add(f"{bucket}:{name}")

    if len(seq_lengths) >= 2 and len(set(seq_lengths)) > 1:
        buckets.add("seq_lengths_mismatch")

    return tuple(sorted(buckets, key=critical_bucket_sort_key))


def critical_bucket_sort_key(bucket: str) -> Tuple[int, str]:
    kind = bucket.split(":", 1)[0]
    return (CRITICAL_BUCKET_ORDER.get(kind, 100), bucket)


def reject_input_signature(row: Dict[str, Any]) -> Dict[str, Any]:
    inp = row.get("input", {})
    return {
        "input_shape": input_shape(inp),
        "input_features": list(input_features(inp)),
        "critical_buckets": list(critical_buckets(inp if isinstance(inp, dict) else {})),
    }


def signature_key(signature: Dict[str, Any]) -> Tuple[str, Tuple[str, ...]]:
    return (
        signature["input_shape"],
        tuple(signature["input_features"]),
    )


def input_size(input_obj: Any) -> int:
    if isinstance(input_obj, dict):
        total = 0
        for value in input_obj.values():
            _, length = value_kind_and_length(value)
            total += length if length is not None else 1
        return total
    _, length = value_kind_and_length(input_obj)
    return length if length is not None else 1


def critical_rank(row: Dict[str, Any]) -> int:
    buckets = critical_buckets(row.get("input", {}))
    if not buckets:
        return 100
    return min(critical_bucket_sort_key(bucket)[0] for bucket in buckets)


def row_priority(row: Dict[str, Any]) -> Tuple[int, int, int, str]:
    sig = reject_input_signature(row)
    feature_count = len(sig["input_features"]) + len(sig["critical_buckets"])
    return (
        critical_rank(row),
        input_size(row.get("input", {})),
        -feature_count,
        stable_json(row),
    )


def with_metadata(row: Dict[str, Any], stage: str, bucket: str = "") -> Dict[str, Any]:
    out = {
        "input": row.get("input"),
        "signature": reject_input_signature(row),
        "reduction_stage": stage,
    }
    if bucket:
        out["reduction_bucket"] = bucket
    return out


def dedup_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen = set()
    out = []
    for row in rows:
        key = reject_input_key(row)
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def select_critical_boundary_rows(rows: List[Dict[str, Any]], keep_per_bucket: int) -> List[Dict[str, Any]]:
    bucketed: Dict[str, List[Dict[str, Any]]] = {}
    for row in rows:
        for bucket in critical_buckets(row.get("input", {})):
            bucketed.setdefault(bucket, []).append(row)

    selected = []
    selected_keys = set()
    for bucket in sorted(bucketed, key=critical_bucket_sort_key):
        for row in sorted(bucketed[bucket], key=row_priority)[:keep_per_bucket]:
            key = reject_input_key(row)
            if key in selected_keys:
                continue
            selected.append(with_metadata(row, stage="critical_boundary", bucket=bucket))
            selected_keys.add(key)
    return selected


def select_diversity_rows(rows: List[Dict[str, Any]], already_selected: List[Dict[str, Any]], keep_total: int) -> List[Dict[str, Any]]:
    selected = list(already_selected)
    selected_keys = {reject_input_key(row) for row in selected}

    buckets: Dict[Tuple[str, Tuple[str, ...]], List[Dict[str, Any]]] = {}
    for row in rows:
        if reject_input_key(row) in selected_keys:
            continue
        sig = reject_input_signature(row)
        buckets.setdefault(signature_key(sig), []).append(row)

    representatives = []
    for sig_key, bucket_rows in buckets.items():
        best = sorted(bucket_rows, key=row_priority)[0]
        representatives.append((row_priority(best), sig_key, best))

    for _priority, sig_key, row in sorted(representatives, key=lambda item: item[0]):
        if len(selected) >= keep_total:
            break
        key = reject_input_key(row)
        if key in selected_keys:
            continue
        selected.append(with_metadata(row, stage="diversity_fill", bucket=stable_json(sig_key)))
        selected_keys.add(key)

    if len(selected) < keep_total:
        for row in sorted(rows, key=row_priority):
            if len(selected) >= keep_total:
                break
            key = reject_input_key(row)
            if key in selected_keys:
                continue
            selected.append(with_metadata(row, stage="fallback_fill"))
            selected_keys.add(key)

    return selected


def reduce_reject_input_rows(rows: List[Dict[str, Any]], keep_total: int, keep_per_critical_bucket: int) -> List[Dict[str, Any]]:
    deduped = dedup_rows(rows)
    if len(deduped) <= keep_total:
        return [with_metadata(row, stage="keep_all") for row in sorted(deduped, key=row_priority)]

    critical = select_critical_boundary_rows(deduped, keep_per_bucket=keep_per_critical_bucket)
    critical = sorted(critical, key=row_priority)

    if len(critical) >= keep_total:
        return critical[:keep_total]

    return select_diversity_rows(deduped, already_selected=critical, keep_total=keep_total)


def build_lite_reject_inputs(reduced_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [
        {"input": row.get("input")}
        for row in reduced_rows
        if isinstance(row, dict) and isinstance(row.get("input"), dict)
    ]


def build_summary(
    task_id: str,
    source_file: str,
    lite_reject_input_file: str,
    rows: List[Dict[str, Any]],
    reduced_rows: List[Dict[str, Any]],
    skipped: bool,
) -> Dict[str, Any]:
    critical_bucket_names = set()
    signature_keys = set()
    for row in dedup_rows(rows):
        sig = reject_input_signature(row)
        signature_keys.add(signature_key(sig))
        critical_bucket_names.update(sig["critical_buckets"])

    stage_counts: Dict[str, int] = {}
    for row in reduced_rows:
        stage = row.get("reduction_stage", "unknown")
        stage_counts[stage] = stage_counts.get(stage, 0) + 1

    return {
        "task_id": task_id,
        "source_file": source_file,
        "raw_case_count": len(rows),
        "case_count": len(dedup_rows(rows)),
        "reduced_case_count": len(reduced_rows),
        "lite_reject_input_file": lite_reject_input_file,
        "lite_reject_input_case_count": len(build_lite_reject_inputs(reduced_rows)),
        "input_signature_bucket_count": len(signature_keys),
        "critical_bucket_count": len(critical_bucket_names),
        "keep_reject_inputs_per_task": KEEP_REJECT_INPUTS_PER_TASK,
        "keep_per_critical_bucket": KEEP_PER_CRITICAL_BUCKET,
        "stage_counts": stage_counts,
        "skipped": skipped,
        "missing": False,
    }


def process_task(task_dir: Path, output_root: Path, reject_input_rel: Path, force: bool = False) -> Dict[str, Any]:
    task_id = task_dir.name
    source_path = task_dir / reject_input_rel
    source_file = path_for_summary(source_path)
    dst_task_dir = output_root / task_id
    log_dir = dst_task_dir / LOG_DIR_NAME
    reduced_path = log_dir / "reduced_reject_inputs.json"
    lite_reject_input_path = dst_task_dir / LITE_REJECT_INPUT_FILE
    summary_path = log_dir / REJECT_INPUT_SUMMARY_FILE
    lite_reject_input_file = path_for_summary(lite_reject_input_path)

    if reduced_path.exists() and not force:
        reduced_rows = load_json_list(reduced_path)
        if not lite_reject_input_path.exists():
            dst_task_dir.mkdir(parents=True, exist_ok=True)
            save_json(lite_reject_input_path, build_lite_reject_inputs(reduced_rows))
        if summary_path.exists():
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            if isinstance(summary, dict):
                summary["source_file"] = source_file
                summary["lite_reject_input_file"] = lite_reject_input_file
                summary["lite_reject_input_case_count"] = len(build_lite_reject_inputs(reduced_rows))
                summary["skipped"] = True
                save_json(summary_path, summary)
                return summary
        return {
            "task_id": task_id,
            "source_file": source_file,
            "reduced_case_count": len(reduced_rows),
            "lite_reject_input_file": lite_reject_input_file,
            "lite_reject_input_case_count": len(build_lite_reject_inputs(reduced_rows)),
            "skipped": True,
            "missing": False,
        }

    dst_task_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    if not source_path.exists():
        save_json(reduced_path, [])
        save_json(lite_reject_input_path, [])
        summary = {
            "task_id": task_id,
            "source_file": source_file,
            "raw_case_count": 0,
            "case_count": 0,
            "reduced_case_count": 0,
            "lite_reject_input_file": lite_reject_input_file,
            "lite_reject_input_case_count": 0,
            "input_signature_bucket_count": 0,
            "critical_bucket_count": 0,
            "skipped": False,
            "missing": True,
        }
        save_json(summary_path, summary)
        return summary

    rows = load_json_list(source_path)
    reduced_rows = reduce_reject_input_rows(
        rows,
        keep_total=KEEP_REJECT_INPUTS_PER_TASK,
        keep_per_critical_bucket=KEEP_PER_CRITICAL_BUCKET,
    )
    summary = build_summary(
        task_id=task_id,
        source_file=source_file,
        lite_reject_input_file=lite_reject_input_file,
        rows=rows,
        reduced_rows=reduced_rows,
        skipped=False,
    )
    save_json(reduced_path, reduced_rows)
    save_json(lite_reject_input_path, build_lite_reject_inputs(reduced_rows))
    save_json(summary_path, summary)
    return summary


def reduce_reject_inputs(
    source_root: Path = DEFAULT_SOURCE_ROOT,
    output_root: Path = DEFAULT_OUTPUT_ROOT,
    reject_input_rel: Path = DEFAULT_REJECT_INPUT_REL,
    task_pattern: str = "verina_*",
    force: bool = False,
) -> Dict[str, Any]:
    source_root = source_root.resolve()
    output_root = output_root.resolve()
    task_dirs = sorted([p for p in source_root.glob(task_pattern) if p.is_dir()], key=natural_key)
    output_root.mkdir(parents=True, exist_ok=True)

    task_summaries = [
        process_task(
            task_dir=task_dir,
            output_root=output_root,
            reject_input_rel=reject_input_rel,
            force=force,
        )
        for task_dir in task_dirs
    ]

    summary = {
        "source_root": path_for_summary(source_root),
        "output_root": path_for_summary(output_root),
        "reject_input_rel": str(reject_input_rel),
        "task_count": len(task_summaries),
        "missing_count": sum(1 for row in task_summaries if row.get("missing")),
        "skipped_count": sum(1 for row in task_summaries if row.get("skipped")),
        "total_case_count": sum(int(row.get("case_count", 0)) for row in task_summaries),
        "total_reduced_case_count": sum(int(row.get("reduced_case_count", 0)) for row in task_summaries),
        "total_lite_reject_input_case_count": sum(int(row.get("lite_reject_input_case_count", 0)) for row in task_summaries),
        "keep_reject_inputs_per_task": KEEP_REJECT_INPUTS_PER_TASK,
        "keep_per_critical_bucket": KEEP_PER_CRITICAL_BUCKET,
        "tasks": task_summaries,
    }
    summary_dir = output_root / LOG_DIR_NAME
    summary_dir.mkdir(parents=True, exist_ok=True)
    save_json(summary_dir / REJECT_INPUT_SUMMARY_FILE, summary)
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reduce reject inputs with boundary-preserving buckets.")
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--reject-input-rel", type=Path, default=DEFAULT_REJECT_INPUT_REL)
    parser.add_argument("--task-pattern", type=str, default="verina_*")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result = reduce_reject_inputs(
        source_root=args.source_root,
        output_root=args.output_root,
        reject_input_rel=args.reject_input_rel,
        task_pattern=args.task_pattern,
        force=args.force,
    )
    print(json.dumps(
        {
            "source_root": result["source_root"],
            "output_root": result["output_root"],
            "task_count": result["task_count"],
            "missing_count": result["missing_count"],
            "skipped_count": result["skipped_count"],
            "total_case_count": result["total_case_count"],
            "total_reduced_case_count": result["total_reduced_case_count"],
            "total_lite_reject_input_case_count": result["total_lite_reject_input_case_count"],
            "summary_file": str(Path(result["output_root"]) / LOG_DIR_NAME / REJECT_INPUT_SUMMARY_FILE),
        },
        ensure_ascii=False,
        indent=2,
    ))
