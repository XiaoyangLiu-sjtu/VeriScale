import argparse
from tqdm import tqdm
from pathlib import Path
from typing import Any, Dict, List
from src.input.step1_llm_generation import DEFAULT_SYSTEM_PROMPT, generate_candidates
from src.input.step2_type_mutation import mutate_candidates
from src.input.step3_lean_filters import filter_by_syntax, filter_by_precond
from utils import TaskDataLoader, APIModel, natural_key, dedup_input_wrapped, save_json


def process_task(root_dir: Path, model: APIModel, task_dir: Path, rounds: int, candidates_per_round: int, example_limit: int, max_mutations_per_input: int, mutation_multi_step_size: int, mutation_ingredient_prob: float) -> Dict[str, Any]:
    task = TaskDataLoader.load_task_data(task_dir)
    seed_accept_inputs = [{"input": t["input"]} for t in task.tests]
    seed_reject_inputs = [{"input": r["input"]} for r in task.reject_inputs]
    seed_candidates: List[Dict[str, Dict[str, Any]]] = dedup_input_wrapped(seed_accept_inputs + seed_reject_inputs)

    step1_llm_candidates = generate_candidates(model=model, task=task, rounds=rounds, candidates_per_round=candidates_per_round, example_limit=example_limit)
    step1_candidates = dedup_input_wrapped(seed_candidates + step1_llm_candidates)

    step2_mutated = mutate_candidates(task=task, candidates=step1_candidates, max_mutations_per_input=max_mutations_per_input, max_multi_step_size=mutation_multi_step_size, ingredient_prob=mutation_ingredient_prob)
    step2_candidates = dedup_input_wrapped(step1_candidates + step2_mutated)

    step3_syntax_ok, step3_syntax_error = filter_by_syntax(root_dir=root_dir, task=task, candidates=step2_candidates)
    tqdm.write(f"[{task_dir.name}] : syntax_ok={len(step3_syntax_ok)}, syntax_error={len(step3_syntax_error)}")

    step3_accept, step3_reject, step3_unknown = filter_by_precond(root_dir=root_dir, task=task, syntax_ok_candidates=step3_syntax_ok)
    tqdm.write(f"[{task_dir.name}] : accept={len(step3_accept)}, reject={len(step3_reject)}, unknown={len(step3_unknown)}")

    stats = {
        "task_id": task.data_id,
        "original_accept_inputs": len(seed_accept_inputs),
        "original_reject_inputs": len(seed_reject_inputs),
        "step1_generated_inputs": len(step1_llm_candidates),
        "step2_mutated_inputs": len(step2_mutated),
        "step3_syntax_ok_inputs": len(step3_syntax_ok),
        "step3_syntax_error_inputs": len(step3_syntax_error),
        "step3_accept_inputs": len(step3_accept),
        "step3_reject_inputs": len(step3_reject),
        "step3_unknown_inputs": len(step3_unknown)
    }

    output_dir = task_dir / "original"
    output_dir.mkdir(parents=True, exist_ok=True)
    save_json(output_dir / "total_inputs.json", step3_syntax_ok)
    save_json(output_dir / "accept_inputs.json", step3_accept)
    save_json(output_dir / "reject_inputs.json", step3_reject)
    save_json(output_dir / "unknown_inputs.json", step3_unknown)
    save_json(output_dir / "expansion_summary_inputs.json", stats)
    return stats


def run_pipeline(args) -> None:
    root_dir = Path(__file__).resolve().parent
    dataset_root = Path(args.dataset_root) if args.dataset_root else (root_dir / "dataset" / "verina")
    task_dirs = sorted([d for d in dataset_root.glob(args.task_pattern) if d.is_dir()], key=natural_key)

    all_stats = []
    model = APIModel(system_prompt=DEFAULT_SYSTEM_PROMPT, model_name=args.model_name, api_key=args.api_key, base_url=args.base_url)
    for task_dir in tqdm(task_dirs, desc="Expanding inputs"):
        try:
            stats = process_task(root_dir=root_dir, model=model, task_dir=task_dir, rounds=args.rounds, candidates_per_round=args.candidates_per_round, example_limit=args.example_limit, max_mutations_per_input=args.max_mutations_per_input, mutation_multi_step_size=args.mutation_multi_step_size, mutation_ingredient_prob=args.mutation_ingredient_prob)
            all_stats.append(stats)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            err = {"task_id": task_dir.name, "error": str(e)}
            all_stats.append(err)
            tqdm.write(f"[{task_dir.name}] error: {e}")

    summary_path = dataset_root / "expansion_summary_inputs.json"
    save_json(summary_path, all_stats)


def parse_args():
    parser = argparse.ArgumentParser(description="Input expansion pipeline: generation, mutation, and filters.")
    parser.add_argument("--dataset-root", type=str, default=None)
    parser.add_argument("--task-pattern", type=str, default="verina_*")
    parser.add_argument("--model-name", type=str, default="gpt-5.3-codex")
    parser.add_argument("--base-url", type=str, default="xxx")
    parser.add_argument("--api-key", type=str, default="xxx")
    parser.add_argument("--rounds", type=int, default=1)
    parser.add_argument("--candidates-per-round", type=int, default=40)
    parser.add_argument("--example-limit", type=int, default=5)
    parser.add_argument("--max-mutations-per-input", type=int, default=15)
    parser.add_argument("--mutation-multi-step-size", type=int, default=5)
    parser.add_argument("--mutation-ingredient-prob", type=float, default=0.3)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_pipeline(args)
