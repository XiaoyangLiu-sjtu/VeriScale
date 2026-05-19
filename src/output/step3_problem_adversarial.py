import re
import json
import utils
from pathlib import Path
from typing import Any, Dict, List
from src.output.prompt_config_adversarial import STEP3_SYSTEM_PROMPT_ADVERSARIAL, STEP3_USER_PROMPT_ADVERSARIAL


_ADVERSARIAL_MARKER_PATTERN = re.compile(r"(?mi)^\s*--\s*Adversarial\s+Implementation\s+(\d+)\s*$")
_NEXT_DECL_PATTERN = re.compile(r"(?m)^(?:def|theorem|lemma|example|abbrev|opaque|axiom)\s+\w+\b")


def _extract_adversarial(model_response, impl_signature=""):
    code_blocks = re.findall(r"```lean\s*(.*?)```", model_response, flags=re.DOTALL | re.IGNORECASE)
    candidates = [block.strip() for block in code_blocks if block.strip()]
    if not candidates:
        candidates = [model_response]

    extracted_funcs = {}
    for code in candidates:
        markers = list(_ADVERSARIAL_MARKER_PATTERN.finditer(code))
        for idx, marker in enumerate(markers):
            func_id = int(marker.group(1))
            start = marker.end()
            end = markers[idx + 1].start() if idx + 1 < len(markers) else len(code)
            block = code[start:end]
            cleaned_segment = utils.strip_hash_comments(block).strip()
            if cleaned_segment:
                extracted_funcs[func_id] = cleaned_segment

    if not extracted_funcs:
        return []
    return [extracted_funcs[fid] for fid in sorted(extracted_funcs.keys())]


def generate_adversarial(problem_description, pred_spec, impl_signature, model_name, api_key, base_url):
    api_llm = utils.APIModel(STEP3_SYSTEM_PROMPT_ADVERSARIAL, model_name, api_key, base_url)
    messages = api_llm.get_messages(
        STEP3_USER_PROMPT_ADVERSARIAL.format(
            problem_description=problem_description,
            pre_condition=pred_spec["pre_condition"],
            post_condition=pred_spec["post_condition"],
            impl_signature=impl_signature,
        )
    )
    adversarial_codes = api_llm.generate_with_retries(
        messages,
        lambda x: _extract_adversarial(x, impl_signature=impl_signature),
        lambda x: bool(x),
        "step3_adversarial_generation",
    )

    if adversarial_codes is not None:
        return adversarial_codes
    return ["Failed to call the LLM; this step failed."] * 5


def dedup_adversarial(adversarial_codes):
    unique_codes = []
    seen = set()
    for code in adversarial_codes or []:
        if not isinstance(code, str):
            continue
        cleaned = code.strip()
        if not cleaned or cleaned in seen:
            continue
        seen.add(cleaned)
        unique_codes.append(cleaned)
    return unique_codes


def normalize_adversarial_func_name(code: str) -> str:
    if not isinstance(code, str):
        return ""
    text = code.strip()
    if not text:
        return ""

    match = re.search(r"(?m)^(\s*def\s+)([^\s(:=]+)", text)
    if not match:
        return text

    func_name = match.group(2)
    normalized_name = re.sub(r"[1-5]$", "", func_name)
    if normalized_name == func_name:
        return text
    start, end = match.span(2)
    return text[:start] + normalized_name + text[end:]


def _load_task_meta_for_compile(task_dir: Path) -> Dict[str, Any]:
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
    lean_data = utils.TaskDataLoader.parse_benchmark_lean_data(raw_lean, signature["name"])

    # Build a source without proof-related sections (proof_aux/proof theorem body).
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
        "lean_source": lean_source,
    }


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


def compile_adversarial_codes(root_dir: Path, task_dir: Path, adversarial_codes: List[str]) -> Dict[str, Any]:
    task_meta = _load_task_meta_for_compile(task_dir)
    rows: List[Dict[str, Any]] = []
    compile_errors: List[Dict[str, Any]] = []

    for idx, code in enumerate(adversarial_codes):
        try:
            lean_content = _replace_target_def(task_meta["lean_source"], task_meta["name"], code)
            ok, msg = utils.run_lean_check(root_dir=root_dir, lean_content=lean_content)
            rows.append(
                {
                    "adversarial_func": code,
                    "compile_ok": bool(ok),
                }
            )
            if ok:
                continue
            else:
                compile_errors.append(
                    {
                        "adversarial_index": idx,
                        "adversarial_func": code,
                        "error": msg,
                    }
                )
        except Exception as e:
            rows.append(
                {
                    "adversarial_func": code,
                    "compile_ok": False,
                }
            )
            compile_errors.append({"adversarial_index": idx, "adversarial_func": code, "error": str(e)})

    return {
        "rows": rows,
        "compile_errors": compile_errors,
    }


def load_existing_step3_rows(dataset_root: Path, task_ids: List[str], output_dir_name: str) -> List[Dict[str, Any]]:
    _ = output_dir_name
    summary_by_task = utils._load_dataset_summary_map(dataset_root)
    rows: List[Dict[str, Any]] = []
    for task_id in task_ids:
        details = summary_by_task.get(task_id, {})
        codes = details.get("step3_problem_adversarial", [])
        if not isinstance(codes, list):
            codes = []
        cleaned_codes: List[str] = []
        for item in codes:
            if not isinstance(item, dict):
                continue
            if not bool(item.get("compile_ok", False)):
                continue
            func = item.get("adversarial_func", "")
            if not isinstance(func, str):
                continue
            cleaned = normalize_adversarial_func_name(func)
            if cleaned:
                cleaned_codes.append(cleaned)
        rows.append({"task_id": task_id, "problem_adversarial": dedup_adversarial(cleaned_codes)})
    rows.sort(key=lambda x: utils.natural_key(Path(x["task_id"])))
    return rows
