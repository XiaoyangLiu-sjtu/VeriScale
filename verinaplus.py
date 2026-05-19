import json
import shutil
from pathlib import Path
from typing import Dict, List


def build_verinaplus_dataset(src_root: Path | None = None, dst_root: Path | None = None) -> Dict[str, int | List[str]]:
    """
    Copy selected files from dataset/verina to dataset/verinaplus.

    For each task directory under src_root (verina_*):
    - copy: description.txt, signature.json, task.json, task.lean
    - copy from plus/: coverage_report.md, reject_inputs.json
    - copy from plus/test.json after removing any element with:
      unexpected == []
    """
    repo_root = Path(__file__).resolve().parent
    src_root = src_root or (repo_root / "dataset" / "verina")
    dst_root = dst_root or (repo_root / "dataset" / "verinaplus")
    src_root = Path(src_root).resolve()
    dst_root = Path(dst_root).resolve()

    if not src_root.exists():
        raise FileNotFoundError(f"Source dataset root not found: {src_root}")
    dst_root.mkdir(parents=True, exist_ok=True)

    required_root_files = ["description.txt", "signature.json", "task.json", "task.lean"]
    required_plus_files = ["coverage_report.md", "test.json", "reject_inputs.json"]

    task_dirs = sorted([p for p in src_root.glob("verina_*") if p.is_dir()], key=lambda x: x.name)
    missing: List[str] = []
    copied = 0
    filtered_test_rows = 0

    for task_dir in task_dirs:
        dst_task_dir = dst_root / task_dir.name
        dst_task_dir.mkdir(parents=True, exist_ok=True)

        # Copy root files.
        for name in required_root_files:
            src_file = task_dir / name
            dst_file = dst_task_dir / name
            if not src_file.exists():
                msg = f"Missing required file: {src_file}"
                print(msg)
                missing.append(msg)
                continue
            shutil.copy2(src_file, dst_file)

        # Copy plus files except test.json (needs filtering).
        for name in required_plus_files:
            src_file = task_dir / "plus" / name
            dst_file = dst_task_dir / name
            if not src_file.exists():
                msg = f"Missing required file: {src_file}"
                print(msg)
                missing.append(msg)
                continue

            if name != "test.json":
                shutil.copy2(src_file, dst_file)
                continue

            try:
                rows = json.loads(src_file.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                msg = f"test.json is invalid JSON: {src_file}"
                print(msg)
                missing.append(msg)
                continue
            if not isinstance(rows, list):
                msg = f"test.json is not a list: {src_file}"
                print(msg)
                missing.append(msg)
                continue

            cleaned = []
            for row in rows:
                if isinstance(row, dict) and row.get("unexpected") == []:
                    filtered_test_rows += 1
                    continue
                cleaned.append(row)

            dst_file.write_text(json.dumps(cleaned, ensure_ascii=False, indent=4) + "\n", encoding="utf-8")

        copied += 1

    return {
        "tasks_total": len(task_dirs),
        "tasks_processed": copied,
        "filtered_test_rows": filtered_test_rows,
        "missing_count": len(missing),
        "missing": missing,
    }


if __name__ == "__main__":
    summary = build_verinaplus_dataset()
    print(json.dumps(summary, ensure_ascii=False, indent=2))
