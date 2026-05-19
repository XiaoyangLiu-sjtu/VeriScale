import argparse
from tqdm import tqdm
from pathlib import Path
from typing import Any, Dict, List
from src.output.step1_problem_model import generate_problem_model, load_existing_step1_results
from src.output.step2_problem_spec import compile_pred_spec, generate_spec, load_existing_compile_rows
from src.output.step3_problem_adversarial import compile_adversarial_codes, dedup_adversarial, generate_adversarial, load_existing_step3_rows, normalize_adversarial_func_name
from src.output.step4_accept_output import generate_accept_outputs_from_impl
from src.output.step5_reject_output import generate_reject_outputs_from_adversarial
from utils import TASK_OUTPUT_SUMMARY_FILE, TaskData, TaskDataLoader, _build_adversarial_details_overrides, _load_dataset_summary_map, _load_or_init_task_summary, _save_dataset_summary, extract_def_signature, natural_key, parallel_map, save_json


LLM_WORKERS = 10
COMPILE_WORKERS = 30


def run_step1_problem_model(task_ids: List[str], tasks_by_id: Dict[str, TaskData], args) -> Dict[str, Dict[str, Any]]:
    def _worker(task_id: str) -> Dict[str, Any]:
        task = tasks_by_id[task_id]
        problem_model = generate_problem_model(problem_description=task.description, model_name=args.step1_model, api_key=args.api_key, base_url=args.base_url)
        return {
            "task_id": task_id,
            "problem_description": task.description,
            "problem_model": problem_model,
        }

    rows = parallel_map(task_ids, _worker, LLM_WORKERS, "Step1 problem_model")
    return {row["task_id"]: row for row in rows}


def run_step2_problem_spec(root_dir: Path, task_ids: List[str],  tasks_by_id: Dict[str, TaskData], step1_results: Dict[str, Dict[str, Any]], step2_models: List[str], args) -> List[Dict[str, Any]]:
    def _worker(job: Dict[str, Any]) -> Dict[str, Any]:
        task = tasks_by_id[job["task_id"]]
        function_signature = {"precond_signature": extract_def_signature(task.lean_data.precond), "postcond_signature": extract_def_signature(task.lean_data.postcond)}
        problem_spec = generate_spec(problem_description=job["problem_description"], problem_model=job["problem_model"], spec_signature=function_signature, model_name=job["step2_model"], api_key=args.api_key, base_url=args.base_url)
        return {
            "task_id": job["task_id"],
            "step2_model": job["step2_model"],
            "problem_description": job["problem_description"],
            "problem_model": job["problem_model"],
            "problem_spec": problem_spec,
        }

    jobs: List[Dict[str, Any]] = []
    for task_id in task_ids:
        s1 = step1_results.get(task_id)
        for model_name in step2_models:
            jobs.append(
                {
                    "task_id": task_id,
                    "step2_model": model_name,
                    "problem_description": s1["problem_description"],
                    "problem_model": s1["problem_model"],
                }
            )

    def _compile_worker(row: Dict[str, Any]) -> Dict[str, Any]:
        task = tasks_by_id[row["task_id"]]
        compile_ok = compile_pred_spec(root_dir=root_dir, task=task, pred_spec=row.get("problem_spec", {}))
        out = dict(row)
        out["compile_ok"] = compile_ok
        return out

    step2_rows = parallel_map(jobs, _worker, LLM_WORKERS, "Step2 problem_spec")
    compile_rows = parallel_map(step2_rows, _compile_worker, COMPILE_WORKERS, "Step2 compile")
    compile_rows.sort(key=lambda x: (natural_key(Path(x["task_id"])), x["step2_model"]))
    return compile_rows


def run_step3_problem_adversarial(root_dir: Path, dataset_root: Path, compile_rows: List[Dict[str, Any]], tasks_by_id: Dict[str, TaskData], args) -> List[Dict[str, Any]]:
    def _worker(row: Dict[str, Any]) -> Dict[str, Any]:
        task = tasks_by_id[row["task_id"]]
        code_signature = extract_def_signature(task.lean_data.code)
        own_codes = generate_adversarial(problem_description=row["problem_description"], pred_spec=row["problem_spec"], impl_signature=code_signature, model_name=args.step3_model, api_key=args.api_key, base_url=args.base_url)
        own_codes = [normalize_adversarial_func_name(c) for c in own_codes if isinstance(c, str)]
        own_codes = dedup_adversarial(own_codes)
        compile_result = compile_adversarial_codes(root_dir=root_dir, task_dir=dataset_root / row["task_id"], adversarial_codes=own_codes)
        compiled_rows = compile_result.get("rows", [])
        compile_errors = compile_result.get("compile_errors", [])
        compile_ok_count = len(
            [
                it
                for it in compiled_rows
                if isinstance(it, dict)
                and bool(it.get("compile_ok", False))
                and isinstance(it.get("adversarial_func"), str)
                and it.get("adversarial_func", "").strip()
            ]
        )
        return {
            "task_id": row["task_id"],
            "problem_adversarial": compiled_rows,
            "step2_model": row.get("step2_model", ""),
            "step3_candidates_before_compile": len(own_codes),
            "step3_candidates_after_compile": compile_ok_count,
            "step3_compile_errors": compile_errors[:20],
        }

    jobs = [r for r in compile_rows if r.get("compile_ok")]
    step3_rows = parallel_map(jobs, _worker, LLM_WORKERS, "Step3 problem_adversarial")
    for row in step3_rows:
        print(
            f"[{row.get('task_id', '')}][{row.get('step2_model', '')}] "
            f"step3_compile_ok={row.get('step3_candidates_after_compile', 0)}/{row.get('step3_candidates_before_compile', 0)}"
        )
    step3_rows.sort(key=lambda x: natural_key(Path(x["task_id"])))
    return step3_rows


def run_step4_accept_outputs(root_dir: Path, dataset_root: Path, task_dirs: List[Path], output_dir_name: str) -> None:
    for task_dir in tqdm(task_dirs, desc="Step4 accept outputs", unit="task"):
        output_dir = task_dir / output_dir_name
        output_dir.mkdir(parents=True, exist_ok=True)
        task_summary = _load_or_init_task_summary(output_dir, task_dir.name)
        accept_summary = generate_accept_outputs_from_impl(task_dir=task_dir, root_dir=root_dir, accept_inputs_rel=f"{output_dir_name}/accept_inputs.json", output_rel=f"{output_dir_name}/test.json", workers=COMPILE_WORKERS)
        task_summary["expand_accept_inputs_number"] = accept_summary.get("accept_inputs", 0)
        task_summary["step4_accept_outputs_number"] = accept_summary.get("accept_outputs", 0)
        task_summary["step4_accept_errors_number"] = accept_summary.get("errors", 0)
        task_summary["step4_accept_error_details"] = accept_summary.get("error_details", [])
        save_json(output_dir / TASK_OUTPUT_SUMMARY_FILE, task_summary)
        print(f"[{task_summary['task_id']}] accept_outputs={task_summary['step4_accept_outputs_number']} accept_errors={task_summary['step4_accept_errors_number']}")
    _save_dataset_summary(dataset_root=dataset_root, task_dirs=task_dirs, output_dir_name=output_dir_name)


def run_step5_reject_outputs(root_dir: Path, dataset_root: Path, task_dirs: List[Path], output_dir_name: str) -> None:
    summary_by_task = _load_dataset_summary_map(dataset_root)
    for task_dir in task_dirs[83:84]:
        output_dir = task_dir / output_dir_name
        output_dir.mkdir(parents=True, exist_ok=True)
        task_summary = _load_or_init_task_summary(output_dir, task_dir.name)
        details = summary_by_task.get(task_dir.name, {})
        raw_adversarial = details.get("step3_problem_adversarial", [])
        adversarial_codes: List[str] = []
        if isinstance(raw_adversarial, list):
            for item in raw_adversarial:
                if not isinstance(item, dict):
                    continue
                if not bool(item.get("compile_ok", False)):
                    continue
                func = item.get("adversarial_func", "")
                if isinstance(func, str) and func.strip():
                    adversarial_codes.append(func)
        reject_summary = generate_reject_outputs_from_adversarial(
            task_dir=task_dir,
            root_dir=root_dir,
            test_rel=f"{output_dir_name}/test.json",
            map_rel=f"{output_dir_name}/map_reject_outputs.json",
            workers=COMPILE_WORKERS,
            adversarial_codes=adversarial_codes,
        )
        task_summary["step5_reject_outputs_number"] = reject_summary.get("total_unexpected_values", 0)
        task_summary["step5_reject_errors_number"] = reject_summary.get("errors", 0)
        task_summary["step5_reject_error_details"] = reject_summary.get("error_details", [])
        save_json(output_dir / TASK_OUTPUT_SUMMARY_FILE, task_summary)
        print(f"[{task_summary['task_id']}] reject_outputs={task_summary['step5_reject_outputs_number']} reject_errors={task_summary['step5_reject_errors_number']}")
    _save_dataset_summary(dataset_root=dataset_root, task_dirs=task_dirs, output_dir_name=output_dir_name)


def run_pipeline(args) -> None:
    root_dir = Path(__file__).resolve().parent
    dataset_root = Path(args.dataset_root) if args.dataset_root else (root_dir / "dataset" / "verina")
    task_dirs = sorted([d for d in dataset_root.glob(args.task_pattern) if d.is_dir()], key=natural_key)

    tasks_by_id: Dict[str, TaskData] = {}
    for task_dir in tqdm(task_dirs, desc="Adversarial: loading tasks", unit="task"):
        task = TaskDataLoader.load_task_data(task_dir)
        tasks_by_id[task.data_id] = task
    task_ids = sorted(tasks_by_id.keys(), key=lambda x: natural_key(Path(x)))

    if not args.skip_step1_problem_model:
        step1_results = run_step1_problem_model(task_ids=task_ids, tasks_by_id=tasks_by_id, args=args)
        _save_dataset_summary(dataset_root=dataset_root, task_dirs=task_dirs, output_dir_name=args.output_dir_name, details_overrides=_build_adversarial_details_overrides(dataset_root=dataset_root, task_ids=task_ids, output_dir_name=args.output_dir_name, step1_results=step1_results, compile_rows=[], step3_rows=[]))
    step1_results = load_existing_step1_results(dataset_root=dataset_root, task_ids=task_ids, tasks_by_id=tasks_by_id, output_dir_name=args.output_dir_name)

    if not args.skip_step2_problem_spec:
        step2_models = [m.strip() for m in (args.step2_models or []) if m.strip()]
        compile_rows = run_step2_problem_spec(root_dir=root_dir, task_ids=task_ids, tasks_by_id=tasks_by_id, step1_results=step1_results, step2_models=step2_models, args=args)
        _save_dataset_summary(dataset_root=dataset_root, task_dirs=task_dirs, output_dir_name=args.output_dir_name, details_overrides=_build_adversarial_details_overrides(dataset_root=dataset_root, task_ids=task_ids, output_dir_name=args.output_dir_name, step1_results=step1_results, compile_rows=compile_rows, step3_rows=[]))
    compile_rows = load_existing_compile_rows(dataset_root=dataset_root, task_ids=task_ids, step1_results=step1_results, output_dir_name=args.output_dir_name)

    if not args.skip_step3_problem_adversarial:
        step3_rows = run_step3_problem_adversarial(root_dir=root_dir, dataset_root=dataset_root, compile_rows=compile_rows, tasks_by_id=tasks_by_id, args=args)
        _save_dataset_summary(dataset_root=dataset_root, task_dirs=task_dirs, output_dir_name=args.output_dir_name, details_overrides=_build_adversarial_details_overrides( dataset_root=dataset_root, task_ids=task_ids, output_dir_name=args.output_dir_name, step1_results=step1_results, compile_rows=compile_rows, step3_rows=step3_rows))
    step3_rows = load_existing_step3_rows(dataset_root=dataset_root, task_ids=task_ids, output_dir_name=args.output_dir_name)

    if not args.skip_step4_accept_outputs:
        run_step4_accept_outputs(root_dir=root_dir, dataset_root=dataset_root, task_dirs=task_dirs, output_dir_name=args.output_dir_name)
    if not args.skip_step5_reject_outputs:
        run_step5_reject_outputs(root_dir=root_dir, dataset_root=dataset_root, task_dirs=task_dirs, output_dir_name=args.output_dir_name)
    _save_dataset_summary(dataset_root=dataset_root, task_dirs=task_dirs, output_dir_name=args.output_dir_name)


def parse_args():
    parser = argparse.ArgumentParser(description="Output pipeline: adversarial preparation, accept outputs, and reject outputs.")
    parser.add_argument("--dataset-root", type=str, default=None, help="Dataset root, default is <repo>/dataset/verina")
    parser.add_argument("--task-pattern", type=str, default="verina_*", help="Glob under dataset-root")
    parser.add_argument("--output-dir-name", type=str, default="plus", help="Per-task output directory name")
    parser.add_argument("--step1-model", type=str, default="gpt-5.3-codex")
    parser.add_argument("--step2-models", nargs="+", default=["claude-haiku-4-5", "claude-sonnet-4-5", "gpt-5.1", "gpt-4.1", "qwen3-max", "deepseek-v3.2"])
    parser.add_argument("--step3-model", type=str, default="gpt-5.3-codex")
    parser.add_argument("--base-url", type=str, default="xxx")
    parser.add_argument("--api-key", type=str, default="xxx")
    parser.add_argument("--skip-step1-problem-model", action="store_true", help="Skip step1: problem_model generation")
    parser.add_argument("--skip-step2-problem-spec", action="store_true", help="Skip step2: problem_spec generation and compile check")
    parser.add_argument("--skip-step3-problem-adversarial", action="store_true", help="Skip step3: adversarial function generation")
    parser.add_argument("--skip-step4-accept-outputs", action="store_true", help="Skip step4: generating expected outputs from accept inputs")
    parser.add_argument("--skip-step5-reject-outputs", action="store_true", help="Skip step5: generating reject outputs from adversarial functions")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_pipeline(args)
