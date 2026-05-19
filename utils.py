import re
import uuid
import json
import shlex
import subprocess
from tqdm import tqdm
from pathlib import Path
from openai import OpenAI
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, TypeVar
from concurrent.futures import ThreadPoolExecutor, as_completed


LEAN_SUBPROCESS_MEMORY_LIMIT_KB = 20 * 1024 * 1024
TASK_OUTPUT_SUMMARY_FILE = "expansion_summary_outputs.json"
T = TypeVar("T")
R = TypeVar("R")


@dataclass
class SignatureParam:
    param_name: str
    param_type: str


@dataclass
class Signature:
    name: str
    parameters: List[SignatureParam]
    return_type: str


@dataclass
class BenchmarkLeanData:
    task_imports: str
    solution_imports: str
    task_aux: str
    solution_aux: str
    precond_aux: str
    precond: str
    code_aux: str
    code: str
    postcond_aux: str
    postcond: str


@dataclass
class TaskData:
    data_id: str
    description: str
    signature: Signature
    lean_data: BenchmarkLeanData
    tests: List[Dict[str, Any]]
    reject_inputs: List[Dict[str, Any]]


class TaskDataLoader:
    _SECTION_PATTERN = re.compile(r"--\s*!benchmark\s*@start\s+([^\n]+)\n([\s\S]*?)--\s*!benchmark\s*@end\s+([^\n]+)", re.MULTILINE)
    _NEXT_DECL_PATTERN = re.compile(r"(?m)^(?:def|theorem|lemma|example|abbrev|opaque|axiom)\s+\w+\b")
    _BENCHMARK_MARKER_LINE_PATTERN = re.compile(r"^\s*--\s*!benchmark\s*@(?:start|end)\s+[^\n]+\s*$")

    @staticmethod
    def _strip_benchmark_marker_lines(text: str) -> str:
        lines = []
        for line in text.splitlines():
            if TaskDataLoader._BENCHMARK_MARKER_LINE_PATTERN.match(line):
                continue
            lines.append(line)
        return "\n".join(lines).strip("\n")

    @staticmethod
    def extract_named_def(raw_lean_data: str, def_name: str, section_name: str = "") -> str:
        m = re.search(rf"(?m)^def\s+{re.escape(def_name)}\b", raw_lean_data)
        if not m:
            return ""

        start = m.start()
        prefix = raw_lean_data[:start]
        lines = prefix.splitlines(keepends=True)
        attr_prefix = ""
        idx = len(lines) - 1
        while idx >= 0:
            prev = lines[idx]
            if prev.strip().startswith("@["):
                attr_prefix = prev + attr_prefix
                idx -= 1
                continue
            break

        if attr_prefix:
            start -= len(attr_prefix)

        next_decl = TaskDataLoader._NEXT_DECL_PATTERN.search(raw_lean_data[m.end():])
        if next_decl:
            end = m.end() + next_decl.start()
        else:
            end = len(raw_lean_data)

        if section_name:
            section_end_pattern = re.compile(
                rf"(?m)^\s*--\s*!benchmark\s*@end\s+{re.escape(section_name)}\b[^\n]*\n?"
            )
            section_end_match = section_end_pattern.search(raw_lean_data[m.end():end])
            if section_end_match:
                end = m.end() + section_end_match.end()

        return TaskDataLoader._strip_benchmark_marker_lines(raw_lean_data[start:end])

    @classmethod
    def extract_precond(cls, raw_lean_data: str, signature_name: str) -> str:
        return cls.extract_named_def(raw_lean_data, f"{signature_name}_precond", "precond")

    @classmethod
    def extract_code(cls, raw_lean_data: str, signature_name: str) -> str:
        return cls.extract_named_def(raw_lean_data, signature_name, "code")

    @classmethod
    def extract_postcond(cls, raw_lean_data: str, signature_name: str) -> str:
        return cls.extract_named_def(raw_lean_data, f"{signature_name}_postcond", "postcond")

    @classmethod
    def parse_benchmark_lean_data(cls, raw_lean_data: str, signature_name: str) -> BenchmarkLeanData:
        sections: Dict[str, str] = {}
        imports_task = ""
        imports_solution = ""

        for match in cls._SECTION_PATTERN.finditer(raw_lean_data):
            start_tag = match.group(1).strip()
            content = match.group(2)
            end_tag = match.group(3).strip()

            base_name = start_tag.split()[0]
            if end_tag != base_name:
                continue

            if base_name == "import":
                if "type=task" in start_tag:
                    imports_task += "\n" + content.strip() + "\n"
                elif "type=solution" in start_tag:
                    imports_solution += "\n" + content.strip() + "\n"
                continue

            sections[base_name] = content.strip("\n")

        return BenchmarkLeanData(
            task_imports=imports_task.strip(),
            solution_imports=imports_solution.strip(),
            task_aux=sections.get("task_aux", ""),
            solution_aux=sections.get("solution_aux", ""),
            precond_aux=sections.get("precond_aux", ""),
            precond=cls.extract_precond(raw_lean_data, signature_name),
            code_aux=sections.get("code_aux", ""),
            code=cls.extract_code(raw_lean_data, signature_name),
            postcond_aux=sections.get("postcond_aux", ""),
            postcond=cls.extract_postcond(raw_lean_data, signature_name),
        )

    @classmethod
    def load_task_data(cls, task_dir: Path) -> TaskData:
        task_json = task_dir / "task.json"
        if not task_json.exists():
            raise FileNotFoundError(f"task.json not found: {task_dir}")
        task_data = json.loads(task_json.read_text())

        desc_path = task_dir / task_data["description_file"]
        lean_path = task_dir / task_data["lean_file"]
        test_path = task_dir / task_data["test_file"]
        reject_path = task_dir / task_data["reject_inputs_file"]

        signature = Signature(
            name=task_data["signature"]["name"],
            parameters=[
                SignatureParam(param_name=p["param_name"], param_type=p["param_type"])
                for p in task_data["signature"]["parameters"]
            ],
            return_type=task_data["signature"]["return_type"],
        )

        lean_data = cls.parse_benchmark_lean_data(lean_path.read_text(), signature.name)
        tests_raw = json.loads(test_path.read_text()) if test_path.exists() else []
        rejects_raw = json.loads(reject_path.read_text()) if reject_path.exists() else []
        tests = [t for t in tests_raw if isinstance(t, dict) and isinstance(t.get("input"), dict)]
        reject_inputs = [r for r in rejects_raw if isinstance(r, dict) and isinstance(r.get("input"), dict)]

        return TaskData(
            data_id=task_data["id"],
            description=desc_path.read_text().strip(),
            signature=signature,
            lean_data=lean_data,
            tests=tests,
            reject_inputs=reject_inputs,
        )


@dataclass
class InputClassifyResult:
    status: str  # accept | reject | unknown | syntax_error
    syntax_ok: bool
    message: str


class APIModel:
    def __init__(self, system_prompt: str, model_name: str, api_key: str, base_url: str):
        self.system_prompt = system_prompt
        self.model_name = model_name
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def get_messages(self, user_prompt: str):
        if self.model_name != "gpt-5.3-codex":
            return [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        return self.system_prompt + "\n\n" + user_prompt

    def _extract_response_text(self, completion):
        text = getattr(completion, "output_text", None)
        if isinstance(text, str) and text.strip():
            return text

        parts = []
        for item in getattr(completion, "output", []) or []:
            if getattr(item, "type", None) != "message":
                continue
            for content_item in getattr(item, "content", []) or []:
                if getattr(content_item, "type", None) == "output_text":
                    piece = getattr(content_item, "text", "")
                    if piece:
                        parts.append(piece)
        if parts:
            return "".join(parts)

        return "[LLM ERROR]"

    def generate(self, messages):
        if self.model_name != "gpt-5.3-codex":
            try:
                completion = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=messages,
                )
                return completion.choices[0].message.content
            except KeyboardInterrupt:
                raise
            except Exception:
                return "[LLM ERROR]"

        try:
            completion = self.client.responses.create(
                model=self.model_name,
                input=messages,
                reasoning={"effort": "high"},
                text={"verbosity": "medium"},
                stream=False,
            )
            return self._extract_response_text(completion)
        except KeyboardInterrupt:
            raise
        except Exception:
            return "[LLM ERROR]"

    def log_retry_failure(self, step_name, attempt, max_attempts, raw_response):
        if attempt < max_attempts:
            tqdm.write(f"[{step_name}] attempt {attempt}/{max_attempts} failed, retrying...")
        else:
            tqdm.write(f"[{step_name}] all {max_attempts} attempts failed, using fallback result.")
        tqdm.write(f"[{step_name}] raw response: {raw_response}")

    def generate_with_retries(self, messages, parse_response, is_valid_result, step_name, max_attempts=10):
        for attempt in range(1, max_attempts + 1):
            response = self.generate(messages)
            parsed = parse_response(response)
            if is_valid_result(parsed):
                return parsed
            self.log_retry_failure(step_name, attempt, max_attempts, response)
        return None


def natural_key(path_like: Any):
    name = path_like.name if isinstance(path_like, Path) else str(path_like)
    parts = re.split(r"(\d+)", name)
    return [(0, int(p)) if p.isdigit() else (1, p.lower()) for p in parts]


def extract_def_signature(definition_text: str) -> str:
    text = (definition_text or "").strip()
    if not text:
        return ""

    match = re.search(r"(?ms)^\s*def\s+\w+\b.*?:=", text)
    if not match:
        return ""

    signature_with_assign = match.group(0).strip()
    return re.sub(r"\s*:=\s*$", "", signature_with_assign).strip()


def _load_dataset_summary_map(dataset_root: Path) -> Dict[str, Dict[str, Any]]:
    summary_path = dataset_root / "expansion_summary_outputs.json"
    rows = json.loads(summary_path.read_text())
    summary_map: Dict[str, Dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        task_id = row.get("task_id", "")
        if isinstance(task_id, str) and task_id:
            summary_map[task_id] = row
    return summary_map


def _new_task_summary(task_id: str) -> dict:
    return {
        "task_id": task_id,
        "original_accept_outputs": 0,
        "original_reject_outputs": 0,
        "step1_problem_model": {},
        "step2_problem_spec": [],
        "step3_problem_adversarial": [],
        "expand_accept_inputs_number": 0,
        "step4_accept_outputs_number": 0,
        "step4_accept_errors_number": 0,
        "step4_accept_error_details": [],
        "step5_reject_outputs_number": 0,
        "step5_reject_errors_number": 0,
        "step5_reject_error_details": [],
    }


def _load_or_init_task_summary(output_dir: Path, task_id: str) -> dict:
    summary_path = output_dir / TASK_OUTPUT_SUMMARY_FILE
    summary = _new_task_summary(task_id)
    if not summary_path.exists():
        return summary

    try:
        data = json.loads(summary_path.read_text())
    except Exception:
        return summary
    if not isinstance(data, dict):
        return summary

    summary.update(data)

    if not isinstance(summary.get("step1_problem_model"), dict):
        summary["step1_problem_model"] = {}
    if not isinstance(summary.get("step2_problem_spec"), list):
        summary["step2_problem_spec"] = []
    if not isinstance(summary.get("step3_problem_adversarial"), list):
        summary["step3_problem_adversarial"] = []
    if not isinstance(summary.get("step4_accept_error_details"), list):
        summary["step4_accept_error_details"] = []
    if not isinstance(summary.get("step5_reject_error_details"), list):
        summary["step5_reject_error_details"] = []

    summary["task_id"] = task_id
    return summary


def _build_adversarial_details_overrides(
    dataset_root: Path,
    task_ids: List[str],
    output_dir_name: str,
    step1_results: Dict[str, Dict[str, Any]],
    compile_rows: List[Dict[str, Any]],
    step3_rows: List[Dict[str, Any]],
) -> Dict[str, Dict[str, Any]]:
    from src.output.step3_problem_adversarial import normalize_adversarial_func_name

    compile_by_task: Dict[str, List[Dict[str, Any]]] = {}
    step3_by_task: Dict[str, List[Dict[str, Any]]] = {}
    for row in compile_rows:
        task_id = row.get("task_id", "")
        if isinstance(task_id, str) and task_id:
            compile_by_task.setdefault(task_id, []).append(row)
    for row in step3_rows:
        task_id = row.get("task_id", "")
        if isinstance(task_id, str) and task_id:
            step3_by_task.setdefault(task_id, []).append(row)

    details_overrides: Dict[str, Dict[str, Any]] = {}
    for task_id in task_ids:
        task_step1 = step1_results.get(task_id, {})
        task_compile = compile_by_task.get(task_id, [])
        task_step3 = step3_by_task.get(task_id, [])

        step1_problem_model = task_step1.get("problem_model", {}) if isinstance(task_step1, dict) else {}

        step2_problem_spec = []
        for row in task_compile:
            pred_spec = row.get("problem_spec", {}) if isinstance(row, dict) else {}
            step2_problem_spec.append(
                {
                    "test_model": row.get("step2_model", ""),
                    "pre_condition": pred_spec.get("pre_condition", ""),
                    "post_condition": pred_spec.get("post_condition", ""),
                    "compile_ok": bool(row.get("compile_ok", False)),
                }
            )

        # Canonical shape:
        # step3_problem_adversarial = [
        #   {"adversarial_func": "<lean def ...>", "compile_ok": true|false}
        # ]
        step3_status_by_func: Dict[str, bool] = {}
        for row in task_step3:
            for item in row.get("problem_adversarial", []) or []:
                if not isinstance(item, dict):
                    continue
                func = item.get("adversarial_func", "")
                if not isinstance(func, str):
                    continue
                cleaned = normalize_adversarial_func_name(func)
                if not cleaned:
                    continue
                compile_ok = bool(item.get("compile_ok", False))
                prev = step3_status_by_func.get(cleaned, False)
                # If duplicates appear, once compile_ok is true, keep true.
                step3_status_by_func[cleaned] = prev or compile_ok

        step3_problem_adversarial: List[Dict[str, Any]] = [
            {"adversarial_func": func, "compile_ok": ok}
            for func, ok in step3_status_by_func.items()
        ]

        details_overrides[task_id] = {
            "step1_problem_model": step1_problem_model,
            "step2_problem_spec": step2_problem_spec,
            "step3_problem_adversarial": step3_problem_adversarial,
        }
    return details_overrides


def _build_task_snapshot(task_dir: Path, output_dir_name: str, previous_snapshot: Dict[str, Any], details_override: Dict[str, Any]) -> dict:
    task_json_path = task_dir / "task.json"
    task_json = json.loads(task_json_path.read_text())
    test_rel = task_json.get("test_file", "test.json")
    reject_rel = task_json.get("reject_inputs_file", "reject_inputs.json")

    original_accept_path = task_dir / test_rel
    original_reject_path = task_dir / reject_rel
    original_accept = json.loads(original_accept_path.read_text())
    original_reject = json.loads(original_reject_path.read_text())

    output_dir = task_dir / output_dir_name
    previous_snapshot = previous_snapshot if isinstance(previous_snapshot, dict) else {}
    details_override = details_override if isinstance(details_override, dict) else {}
    merged_details = dict(previous_snapshot)
    merged_details.update(details_override)
    stats = _load_or_init_task_summary(output_dir, task_dir.name)
    accept_inputs_path = output_dir / "accept_inputs.json"
    accept_inputs = json.loads(accept_inputs_path.read_text())

    step1_problem_model = merged_details.get("step1_problem_model", stats.get("step1_problem_model", {}))
    if not isinstance(step1_problem_model, dict):
        step1_problem_model = {}

    step2_problem_spec = merged_details.get("step2_problem_spec", stats.get("step2_problem_spec", []))
    if not isinstance(step2_problem_spec, list):
        step2_problem_spec = []

    step3_problem_adversarial = merged_details.get("step3_problem_adversarial", stats.get("step3_problem_adversarial", []))
    if not isinstance(step3_problem_adversarial, list):
        step3_problem_adversarial = []

    step4_error_details = stats.get("step4_accept_error_details", [])
    if not isinstance(step4_error_details, list):
        step4_error_details = []

    step5_error_details = stats.get("step5_reject_error_details", [])
    if not isinstance(step5_error_details, list):
        step5_error_details = []

    return {
        "task_id": task_dir.name,
        "original_accept_outputs": len(original_accept),
        "original_reject_outputs": len(original_reject),
        "step1_problem_model": step1_problem_model,
        "step2_problem_spec": step2_problem_spec,
        "step3_problem_adversarial": step3_problem_adversarial,
        "expand_accept_inputs_number": len(accept_inputs),
        "step4_accept_outputs_number": int(stats.get("step4_accept_outputs_number", 0)),
        "step4_accept_errors_number": int(stats.get("step4_accept_errors_number", 0)),
        "step4_accept_error_details": step4_error_details,
        "step5_reject_outputs_number": int(stats.get("step5_reject_outputs_number", 0)),
        "step5_reject_errors_number": int(stats.get("step5_reject_errors_number", 0)),
        "step5_reject_error_details": step5_error_details,
    }


def _save_dataset_summary(
    dataset_root: Path,
    task_dirs: List[Path],
    output_dir_name: str,
    details_overrides: Dict[str, Dict[str, Any]] = None,
) -> None:
    previous_by_task = _load_dataset_summary_map(dataset_root)
    details_overrides = details_overrides or {}
    all_summaries = []
    for task_dir in task_dirs:
        snapshot = _build_task_snapshot(
            task_dir=task_dir,
            output_dir_name=output_dir_name,
            previous_snapshot=previous_by_task.get(task_dir.name, {}),
            details_override=details_overrides.get(task_dir.name, {}),
        )
        all_summaries.append(snapshot)
        output_dir = task_dir / output_dir_name
        output_dir.mkdir(parents=True, exist_ok=True)
        save_json(output_dir / TASK_OUTPUT_SUMMARY_FILE, snapshot)
    save_json(dataset_root / TASK_OUTPUT_SUMMARY_FILE, all_summaries)


def parallel_map(items: List[T], worker: Callable[[T], R], max_workers: int, desc: str) -> List[R]:
    if not items:
        return []
    results: List[R] = []
    with ThreadPoolExecutor(max_workers=max(1, max_workers)) as executor:
        futures = [executor.submit(worker, item) for item in items]
        for fut in tqdm(as_completed(futures), total=len(futures), desc=desc):
            results.append(fut.result())
    return results


def save_json(path: Path, data: Any):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=4) + "\n")


def dedup_input_wrapped(items: List[Dict[str, Dict[str, Any]]]) -> List[Dict[str, Dict[str, Any]]]:
    seen = set()
    out = []
    for it in items:
        if "input" not in it or not isinstance(it["input"], dict):
            continue
        key = json.dumps(it["input"], ensure_ascii=False, sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        out.append({"input": it["input"]})
    return out


def strip_hash_comments(text: str) -> str:
    if not text:
        return ""
    return "\n".join(line for line in text.splitlines() if not line.strip().startswith("#"))


def run_lean_check(root_dir: Path, lean_content: str, timeout: int = 60, return_raw: bool = False):
    playground_dir = root_dir / "lean-playground"
    playground_dir.mkdir(parents=True, exist_ok=True)
    file_name = f"input_expand_{uuid.uuid4().hex}.lean"
    lean_file = playground_dir / file_name
    lean_file.write_text(lean_content)

    try:
        cmd = (
            f"ulimit -v {LEAN_SUBPROCESS_MEMORY_LIMIT_KB}; "
            f"exec lake lean {shlex.quote(str(lean_file))}"
        )
        result = subprocess.run(
            ["bash", "-lc", cmd],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            cwd=root_dir,
        )
        stdout = result.stdout.decode()
        stderr = result.stderr.decode()
        msg = stdout + "\n" + stderr
        if return_raw:
            return result.returncode == 0, msg, stdout, stderr
        return result.returncode == 0, msg
    except subprocess.TimeoutExpired:
        if return_raw:
            return False, "TIMEOUT", "", "TIMEOUT"
        return False, "TIMEOUT"
    except Exception as e:
        if return_raw:
            return False, f"COMPERROR: {e}", "", f"COMPERROR: {e}"
        return False, f"COMPERROR: {e}"
    finally:
        try:
            lean_file.unlink()
        except FileNotFoundError:
            pass
        except OSError:
            pass
