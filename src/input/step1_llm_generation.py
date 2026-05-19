import re
import json
from typing import Dict, List, Optional, Tuple
from utils import TaskData, APIModel, dedup_input_wrapped


DEFAULT_SYSTEM_PROMPT = """
You are an expert at generating diverse candidate inputs for Lean4 code verification tasks.

Return ONLY a JSON array. Each element must strictly follow:
{"input": {"param1": value1, "param2": value2, ...}}

Rules:
1. Do not output markdown, prose, comments, or code fences.
2. Keys in each `input` object must exactly match the function parameter names: no missing keys, no extra keys.
3. Values must be JSON-serializable and type-compatible with the declared Lean parameter types.
4. Treat the ground-truth precondition as the valid-input boundary: generate both valid and invalid inputs, especially boundary cases.
5. Include both likely-valid and likely-invalid inputs. Treat likely-invalid as semantically violating the precondition, not malformed JSON.
6. Generate diverse and challenging edge-case candidates. Return exactly the number of candidates requested by the user.
"""


def build_user_prompt(task: TaskData, candidate_count: int, example_limit: int) -> str:
    description = task.description.replace("{", "{{").replace("}", "}}")
    precond = task.lean_data.precond.replace("{", "{{").replace("}", "}}")
    parameters = {
        "parameters": [
            {"param_name": p.param_name, "param_type": p.param_type}
            for p in task.signature.parameters
        ],
    }
    test_examples = [{"input": tc["input"]} for tc in task.tests[:example_limit]]
    reject_examples = [{"input": rc["input"]} for rc in task.reject_inputs[:example_limit]]
    
    invalid_target = min(candidate_count, max(2, int(round(candidate_count * 0.2))))
    valid_target = max(0, candidate_count - invalid_target)
    user_prompt = """
Generate candidate inputs for this Lean4 programming verification task.

Task description:
{description}

Ground-truth precondition:
{precond}

Use of precondition:
- It defines the semantic boundary of valid inputs.
- Generate both inputs that satisfy it and inputs that violate it.
- Focus on hard boundary/edge cases around this condition.
- "likely-invalid" means: still valid JSON and type-compatible, but likely violates the precondition.
Validity mix target:
- total candidates: {candidate_count}
- likely-invalid target: {invalid_target}
- likely-valid target: {valid_target}
- If constraints make exact ratio hard, prioritize exact total count and boundary coverage.

Function parameters (JSON):
{parameters}

Example likely-valid inputs:
{test_examples}

Example likely-invalid inputs (maybe no examples available, but generate if possible):
{reject_examples}

Output format MUST be exactly a JSON array of objects:
[{{"input": {{"param": value, ...}}}}, ...]
""".format(
        description=description,
        precond=precond,
        parameters=json.dumps(parameters, ensure_ascii=False, indent=2),
        test_examples=json.dumps(test_examples, ensure_ascii=False, indent=2),
        reject_examples=json.dumps(reject_examples, ensure_ascii=False, indent=2),
        candidate_count=candidate_count,
        invalid_target=invalid_target,
        valid_target=valid_target,
    )
    return user_prompt


def extract_json_array_block(text: str) -> Optional[str]:
    if not text or text == "[LLM ERROR]":
        return None

    stripped = text.strip()
    if stripped.startswith("```"):
        fence_parts = stripped.split("```")
        if len(fence_parts) >= 3:
            stripped = fence_parts[1]
            if stripped.strip().startswith("json"):
                stripped = stripped.strip()[4:].strip()

    if stripped.startswith("[") and stripped.endswith("]"):
        return stripped

    match = re.search(r"\[[\s\S]*\]", stripped)
    if match:
        return match.group(0)
    return None


def parse_candidates_response(response: str) -> Optional[List[Dict[str, Dict[str, object]]]]:
    block = extract_json_array_block(response)
    if block is None:
        return None

    try:
        data = json.loads(block)
    except Exception:
        return None

    if not isinstance(data, list):
        return None

    parsed: List[Dict[str, Dict[str, object]]] = []
    for item in data:
        if isinstance(item, dict) and "input" in item and isinstance(item["input"], dict):
            parsed.append({"input": item["input"]})
        elif isinstance(item, dict):
            parsed.append({"input": item})

    if not parsed:
        return None
    return dedup_input_wrapped(parsed)


def is_valid_candidates(parsed: Optional[List[Dict[str, Dict[str, object]]]]) -> bool:
    return parsed is not None and len(parsed) > 0


def response_parse_validate(parsed) -> List[Dict[str, Dict[str, object]]]:
    if not parsed:
        return []
    return parsed


def generate_one_round(model: APIModel, task: TaskData, round_idx: int, candidates_per_round: int, example_limit: int, max_retry: int) -> Tuple[List[Dict[str, Dict[str, object]]], str]:
    prompt = build_user_prompt(task, candidates_per_round, example_limit)
    messages = model.get_messages(prompt)
    parsed = model.generate_with_retries(
        messages=messages,
        parse_response=parse_candidates_response,
        is_valid_result=is_valid_candidates,
        step_name=f"{task.data_id}:round{round_idx + 1}",
    )
    round_candidates = response_parse_validate(parsed)
    return round_candidates, prompt


def generate_candidates(model: APIModel, task: TaskData, rounds: int, candidates_per_round: int, example_limit: int, max_retry: int) -> List[Dict[str, Dict[str, object]]]:
    generated_candidates: List[Dict[str, Dict[str, object]]] = []
    for round_idx in range(rounds):
        round_candidates, _ = generate_one_round(
            model=model,
            task=task,
            round_idx=round_idx,
            candidates_per_round=candidates_per_round,
            example_limit=example_limit,
        )
        generated_candidates.extend(round_candidates)
    return dedup_input_wrapped(generated_candidates)
