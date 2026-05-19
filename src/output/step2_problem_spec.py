import re
import utils
from pathlib import Path
from typing import Any, Dict, List
from src.output.prompt_config_adversarial import STEP2_SYSTEM_PROMPT, STEP2_USER_PROMPT


_PRE_MARKER_PATTERN = re.compile(r"(?mi)^\s*--\s*Precondition\s+Implementation\s*$")
_POST_MARKER_PATTERN = re.compile(r"(?mi)^\s*--\s*Postcondition\s+Implementation\s*$")


def _extract_spec(model_response, spec_signature=None):
    code_blocks = re.findall(r"```lean\s*(.*?)```", model_response, flags=re.DOTALL | re.IGNORECASE)
    candidates = [block.strip() for block in code_blocks if block.strip()]
    if not candidates:
        candidates = [model_response]

    for code in candidates:
        pre_marker = _PRE_MARKER_PATTERN.search(code)
        post_marker = _POST_MARKER_PATTERN.search(code)
        if not pre_marker or not post_marker:
            continue
        if pre_marker.start() >= post_marker.start():
            continue

        pre_block = code[pre_marker.end() : post_marker.start()]
        post_block = code[post_marker.end() :]

        pre_condition = utils.strip_hash_comments(pre_block).strip()
        post_condition = utils.strip_hash_comments(post_block).strip()
        if not pre_condition or not post_condition:
            continue
        return {"pre_condition": pre_condition, "post_condition": post_condition}

    return {"pre_condition": "", "post_condition": ""}


def generate_spec(problem_description, problem_model, spec_signature, model_name, api_key, base_url):
    api_llm = utils.APIModel(STEP2_SYSTEM_PROMPT, model_name, api_key, base_url)
    messages = api_llm.get_messages(
        STEP2_USER_PROMPT.format(
            problem_description=problem_description,
            input=problem_model["input"],
            output=problem_model["output"],
            precond_signature=spec_signature["precond_signature"],
            postcond_signature=spec_signature["postcond_signature"],
        )
    )
    formal_spec = api_llm.generate_with_retries(
        messages,
        lambda x: _extract_spec(x, spec_signature=spec_signature),
        lambda x: x != {"pre_condition": "", "post_condition": ""},
        "step2_formal_spec_generation",
    )

    if formal_spec is not None:
        return formal_spec
    return {
        "pre_condition": "Failed to call the LLM; this step failed.",
        "post_condition": "Failed to call the LLM; this step failed.",
    }


def build_compile_content(task: utils.TaskData, pred_spec: Dict[str, str]) -> str:
    parts: List[str] = []
    if task.lean_data.task_imports.strip():
        parts.append(task.lean_data.task_imports.strip())
    if task.lean_data.solution_imports.strip():
        parts.append(task.lean_data.solution_imports.strip())

    for block in [task.lean_data.task_aux, task.lean_data.solution_aux]:
        if block.strip():
            parts.append(block.strip())

    parts.append((pred_spec.get("pre_condition") or "").strip())
    parts.append((pred_spec.get("post_condition") or "").strip())
    return "\n\n".join(p for p in parts if p.strip()) + "\n"


def compile_pred_spec(root_dir: Path, task: utils.TaskData, pred_spec: Dict[str, str]) -> bool:
    pre_cond = (pred_spec.get("pre_condition") or "").strip()
    post_cond = (pred_spec.get("post_condition") or "").strip()

    if not pre_cond or not post_cond:
        return False
    if "Failed to call the LLM; this step failed." in pre_cond or "Failed to call the LLM; this step failed." in post_cond:
        return False

    compile_content = build_compile_content(task, pred_spec)
    ok, _ = utils.run_lean_check(root_dir=root_dir, lean_content=compile_content)
    return ok


def load_existing_compile_rows(dataset_root: Path, task_ids: List[str], step1_results: Dict[str, Dict[str, Any]], output_dir_name: str) -> List[Dict[str, Any]]:
    _ = output_dir_name
    summary_by_task = utils._load_dataset_summary_map(dataset_root)
    rows: List[Dict[str, Any]] = []
    for task_id in task_ids:
        details = summary_by_task.get(task_id, {})
        task_step2 = details.get("step2_problem_spec", [])
        if not isinstance(task_step2, list):
            task_step2 = []

        step1 = step1_results.get(task_id, {})
        for item in task_step2:
            if not isinstance(item, dict):
                continue
            rows.append(
                {
                    "task_id": task_id,
                    "step2_model": item.get("test_model", ""),
                    "problem_description": step1.get("problem_description", ""),
                    "problem_model": step1.get("problem_model", {}),
                    "problem_spec": {
                        "pre_condition": item.get("pre_condition", ""),
                        "post_condition": item.get("post_condition", ""),
                    },
                    "compile_ok": bool(item.get("compile_ok", False)),
                }
            )
    rows.sort(key=lambda x: (utils.natural_key(Path(x["task_id"])), x.get("step2_model", "")))
    return rows
