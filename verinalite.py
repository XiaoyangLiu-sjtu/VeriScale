import argparse
import json
import shutil
from pathlib import Path
from typing import Any, Dict, List

from reduce_pairs import reduce_accept
from reduce_unexpected_inputs import reduce_reject_inputs
from utils import natural_key, save_json


DEFAULT_VERINAPLUS_ROOT = Path("dataset") / "verinaplus"
DEFAULT_VERINA_ROOT = Path("dataset") / "verina"
DEFAULT_OUTPUT_ROOT = Path("dataset") / "verinalite"
LOG_DIR_NAME = "log"
TASK_FILES_TO_COPY = [
    "description.txt",
    "signature.json",
    "task.json",
    "task.lean",
]
VERINALITE_SUMMARY_FILE = "verinalite_summary.json"
LEGACY_ROOT_LOG_FILES = [
    "accept_adversarial_counts.json",
    "accept_adversarial_kills.json",
    "accept_lite_selection.json",
    "accept_reduction_summary.json",
    "accept_set_cover.json",
    "reduced_accept.json",
    "reduced_reject_inputs.json",
    "reject_input_reduction_summary.json",
]


def path_for_summary(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path(__file__).resolve().parent))
    except ValueError:
        return str(path)


def copy_task_files(
    verinaplus_root: Path,
    output_root: Path,
    task_pattern: str = "verina_*",
) -> Dict[str, Any]:
    verinaplus_root = verinaplus_root.resolve()
    output_root = output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    task_dirs = sorted([p for p in verinaplus_root.glob(task_pattern) if p.is_dir()], key=natural_key)
    task_summaries: List[Dict[str, Any]] = []
    missing_files: List[str] = []
    copied_file_count = 0

    for task_dir in task_dirs:
        dst_task_dir = output_root / task_dir.name
        dst_task_dir.mkdir(parents=True, exist_ok=True)
        (dst_task_dir / LOG_DIR_NAME).mkdir(parents=True, exist_ok=True)

        copied_files = []
        missing_for_task = []
        for filename in TASK_FILES_TO_COPY:
            src_file = task_dir / filename
            dst_file = dst_task_dir / filename
            if not src_file.exists():
                missing = path_for_summary(src_file)
                missing_files.append(missing)
                missing_for_task.append(missing)
                continue
            shutil.copy2(src_file, dst_file)
            copied_files.append(filename)
            copied_file_count += 1

        task_summaries.append(
            {
                "task_id": task_dir.name,
                "copied_files": copied_files,
                "missing_files": missing_for_task,
            }
        )

    return {
        "verinaplus_root": path_for_summary(verinaplus_root),
        "output_root": path_for_summary(output_root),
        "task_count": len(task_dirs),
        "copied_file_count": copied_file_count,
        "missing_file_count": len(missing_files),
        "missing_files": missing_files,
        "tasks": task_summaries,
    }


def cleanup_legacy_root_logs(output_root: Path, task_pattern: str = "verina_*") -> Dict[str, Any]:
    output_root = output_root.resolve()
    task_dirs = sorted([p for p in output_root.glob(task_pattern) if p.is_dir()], key=natural_key)
    removed_files = []

    for task_dir in task_dirs:
        for filename in LEGACY_ROOT_LOG_FILES:
            path = task_dir / filename
            if not path.exists() or not path.is_file():
                continue
            path.unlink()
            removed_files.append(path_for_summary(path))

    return {
        "removed_file_count": len(removed_files),
        "removed_files": removed_files,
    }


def build_verinalite_dataset(
    verinaplus_root: Path = DEFAULT_VERINAPLUS_ROOT,
    verina_root: Path = DEFAULT_VERINA_ROOT,
    output_root: Path = DEFAULT_OUTPUT_ROOT,
    task_pattern: str = "verina_*",
    force: bool = False,
) -> Dict[str, Any]:
    verinaplus_root = verinaplus_root.resolve()
    verina_root = verina_root.resolve()
    output_root = output_root.resolve()

    copied = copy_task_files(
        verinaplus_root=verinaplus_root,
        output_root=output_root,
        task_pattern=task_pattern,
    )
    accept = reduce_accept(
        accept_root=verinaplus_root,
        adversarial_root=verina_root,
        output_root=output_root,
        task_pattern=task_pattern,
        force=force,
    )
    reject_inputs = reduce_reject_inputs(
        source_root=verina_root,
        output_root=output_root,
        task_pattern=task_pattern,
        force=force,
    )
    cleanup = cleanup_legacy_root_logs(output_root=output_root, task_pattern=task_pattern)

    summary = {
        "verinaplus_root": path_for_summary(verinaplus_root),
        "verina_root": path_for_summary(verina_root),
        "output_root": path_for_summary(output_root),
        "task_pattern": task_pattern,
        "force": force,
        "copied": {
            "task_count": copied["task_count"],
            "copied_file_count": copied["copied_file_count"],
            "missing_file_count": copied["missing_file_count"],
            "missing_files": copied["missing_files"],
        },
        "accept": {
            "task_count": accept["task_count"],
            "summary_file": str(Path(accept["output_root"]) / LOG_DIR_NAME / "accept_adversarial_count_summary.json"),
            "total_lite_test_case_count": sum(
                int(task.get("lite_test_case_count", 0))
                for task in accept.get("tasks", [])
                if isinstance(task, dict)
            ),
        },
        "reject_inputs": {
            "task_count": reject_inputs["task_count"],
            "summary_file": str(Path(reject_inputs["output_root"]) / LOG_DIR_NAME / "reject_input_reduction_summary.json"),
            "total_lite_reject_input_case_count": reject_inputs["total_lite_reject_input_case_count"],
        },
        "cleanup": cleanup,
    }

    log_dir = output_root / LOG_DIR_NAME
    log_dir.mkdir(parents=True, exist_ok=True)
    save_json(log_dir / VERINALITE_SUMMARY_FILE, summary)
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build VerinaLite from VerinaPlus and reduction logs.")
    parser.add_argument("--verinaplus-root", type=Path, default=DEFAULT_VERINAPLUS_ROOT)
    parser.add_argument("--verina-root", type=Path, default=DEFAULT_VERINA_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--task-pattern", type=str, default="verina_*")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result = build_verinalite_dataset(
        verinaplus_root=args.verinaplus_root,
        verina_root=args.verina_root,
        output_root=args.output_root,
        task_pattern=args.task_pattern,
        force=args.force,
    )
    print(json.dumps(
        {
            "verinaplus_root": result["verinaplus_root"],
            "verina_root": result["verina_root"],
            "output_root": result["output_root"],
            "task_pattern": result["task_pattern"],
            "copied_missing_file_count": result["copied"]["missing_file_count"],
            "accept_task_count": result["accept"]["task_count"],
            "reject_input_task_count": result["reject_inputs"]["task_count"],
            "cleanup_removed_file_count": result["cleanup"]["removed_file_count"],
            "summary_file": str(Path(result["output_root"]) / LOG_DIR_NAME / VERINALITE_SUMMARY_FILE),
        },
        ensure_ascii=False,
        indent=2,
    ))
