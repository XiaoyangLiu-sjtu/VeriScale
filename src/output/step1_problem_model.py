import re
import utils
from pathlib import Path
from typing import Any, Dict, List
from src.output.prompt_config_adversarial import STEP1_SYSTEM_PROMPT, STEP1_USER_PROMPT


def _extract_problem_modeling(model_response):
    input_match = re.search(r"^\s*Input\s*:\s*(.*?)(?=^\s*Output\s*:)", model_response, flags=re.DOTALL | re.IGNORECASE | re.MULTILINE)
    output_match = re.search(r"^\s*Output\s*:\s*(.*)$", model_response, flags=re.DOTALL | re.IGNORECASE | re.MULTILINE)
    if not input_match or not output_match:
        return {"input": "", "output": ""}

    input_block = input_match.group(1).strip() if input_match else ""
    output_block = output_match.group(1).strip() if output_match else ""
    if not input_block or not output_block:
        return {"input": "", "output": ""}

    return {
        "input": input_block,
        "output": output_block,
    }


def generate_problem_model(problem_description, model_name, api_key, base_url):
    api_llm = utils.APIModel(STEP1_SYSTEM_PROMPT, model_name, api_key, base_url)
    messages = api_llm.get_messages(STEP1_USER_PROMPT.format(problem_description=problem_description))
    problem_model = api_llm.generate_with_retries(
        messages,
        _extract_problem_modeling,
        lambda x: x != {"input": "", "output": ""},
        "step1_problem_modeling",
    )

    if problem_model is not None:
        return problem_model
    return {
        "input": "Failed to call the LLM; this step failed.",
        "output": "Failed to call the LLM; this step failed.",
    }


def load_existing_step1_results(dataset_root: Path, task_ids: List[str], tasks_by_id: Dict[str, utils.TaskData], output_dir_name: str) -> Dict[str, Dict[str, Any]]:
    _ = output_dir_name
    summary_by_task = utils._load_dataset_summary_map(dataset_root)
    loaded: Dict[str, Dict[str, Any]] = {}
    for task_id in task_ids:
        details = summary_by_task.get(task_id, {})
        problem_model = details.get("step1_problem_model", {})
        if not isinstance(problem_model, dict):
            problem_model = {}
        loaded[task_id] = {
            "task_id": task_id,
            "problem_description": tasks_by_id[task_id].description,
            "problem_model": problem_model,
        }
    return loaded
