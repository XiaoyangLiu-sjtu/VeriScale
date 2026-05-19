# Dataset note (scanned from `dataset/verina/**/task.json`, 189 tasks):
# - unique input param types: 21
# - param-type frequency:
#   Array Int: 66
#   Int: 58
#   List Int: 48
#   Nat: 39
#   String: 23
#   List Nat: 17
#   List Char: 3
#   Array Nat: 3
#   UInt8: 2
#   Char: 2
#   Array Char: 2
#   Map Int Int: 2
#   List (Int): 1
#   List Float: 1
#   Float: 1
#   List (Prod Nat Nat): 1
#   Array (Array Int): 1
#   Array (Array Nat): 1
#   List (List Nat): 1
#   Int -> Bool: 1
#   List (Prod Int Int): 1
#
# This module currently prioritizes mutation coverage for the top-8 frequent types via param-type dispatch:
# Int / Nat / String / List Int / Array Int / List Nat / Array Nat / List Char.


import re
import random
from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Set, Tuple
from utils import TaskData, dedup_input_wrapped


MAX_MULTI_STEP_SIZE = 5
_TYPE_INT = "Int"
_TYPE_NAT = "Nat"
_TYPE_STRING = "String"
_TYPE_LIST_INT = "List Int"
_TYPE_ARRAY_INT = "Array Int"
_TYPE_LIST_NAT = "List Nat"
_TYPE_ARRAY_NAT = "Array Nat"
_TYPE_LIST_CHAR = "List Char"


@dataclass
class MutationConfig:
    max_mutations_per_seed: int = 10
    max_multi_step_size: int = MAX_MULTI_STEP_SIZE
    ingredient_prob: float = 0.35
    seed: int = 42


class EvalPlusStyleMutator:
    def __init__(self, task: TaskData, config: MutationConfig):
        self.task = task
        self.config = config
        self.rng = random.Random(config.seed)
        self.param_types = {
            p.param_name: self._normalize_param_type(p.param_type)
            for p in self.task.signature.parameters
        }

        self.ingredients: Dict[str, Set[Any]] = {
            "int": set(),
            "nat": set(),
            "str": set(),
            "bool": set(),
            "char": set(),
        }

    def _normalize_param_type(self, param_type: str) -> str:
        t = " ".join((param_type or "").split())
        t = re.sub(r"^(List|Array)\s*\(\s*(Int|Nat|Char)\s*\)$", r"\1 \2", t)
        return t

    def _fetch_ingredients_from_value(self, value: Any) -> None:
        if isinstance(value, bool):
            self.ingredients["bool"].add(value)
            return

        if isinstance(value, int):
            self.ingredients["int"].add(value)
            if value >= 0:
                self.ingredients["nat"].add(value)
            return

        if isinstance(value, list):
            for item in value:
                self._fetch_ingredients_from_value(item)
            return

        if isinstance(value, str):
            self.ingredients["str"].add(value)
            if len(value) == 1:
                self.ingredients["char"].add(value)
            for token in value.strip().split():
                self.ingredients["str"].add(token)
                if len(token) == 1:
                    self.ingredients["char"].add(token)

            int_seq = self._parse_numeric_seq_literal(value, allow_negative=True)
            if int_seq is not None:
                for x in int_seq:
                    self.ingredients["int"].add(x)
                    if x >= 0:
                        self.ingredients["nat"].add(x)

            char_seq = self._parse_char_seq_literal(value)
            if char_seq is not None:
                for ch in char_seq:
                    self.ingredients["char"].add(ch)
            return

    def _bootstrap_ingredients(self, candidates: List[Dict[str, Dict[str, Any]]]) -> None:
        for wrapped in candidates:
            inp = wrapped.get("input", {})
            if not isinstance(inp, dict):
                continue
            for v in inp.values():
                self._fetch_ingredients_from_value(v)

    def _pick_ingredient(self, kind: str) -> Any:
        pool = list(self.ingredients.get(kind, set()))
        if not pool:
            return None
        return self.rng.choice(pool)

    def _maybe_use_ingredient(self, kind: str) -> Any:
        if self.rng.random() < self.config.ingredient_prob:
            return self._pick_ingredient(kind)
        return None

    def _mutate_int(self, value: int) -> int:
        ing = self._maybe_use_ingredient("int")
        if isinstance(ing, int):
            return ing
        ops = [
            lambda x: x + self.rng.randint(-2, 2),
            lambda x: -x,
            lambda x: x * 2,
            lambda x: 0,
            lambda x: x + 1,
            lambda x: x - 1,
        ]
        return self.rng.choice(ops)(value)

    def _mutate_nat(self, value: int) -> int:
        ing = self._maybe_use_ingredient("nat")
        if isinstance(ing, int) and ing >= 0:
            return ing
        return max(0, self._mutate_int(max(0, value)))

    def _mutate_bool(self, value: bool) -> bool:
        ing = self._maybe_use_ingredient("bool")
        if isinstance(ing, bool):
            return ing
        return not value

    def _mutate_char(self, value: str) -> str:
        ing = self._maybe_use_ingredient("char")
        if isinstance(ing, str) and len(ing) == 1:
            return ing
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        if value and len(value) == 1 and self.rng.random() < 0.5:
            return value.swapcase() if value.isalpha() else self.rng.choice(alphabet)
        return self.rng.choice(alphabet)

    def _mutate_str(self, value: str) -> str:
        ing = self._maybe_use_ingredient("str")
        if isinstance(ing, str):
            return ing
        ops = [
            lambda s: "",
            lambda s: s + "_x",
            lambda s: s[::-1],
            lambda s: s + " " + self.rng.choice(["0", "1", "edge"]),
        ]
        return self.rng.choice(ops)(value)

    def _parse_seq_literal(self, value: Any) -> Optional[Tuple[List[str], str, str]]:
        if isinstance(value, list):
            return [str(x) for x in value], "", "list"

        if not isinstance(value, str):
            return None

        text = value.strip()
        if not ((text.startswith("#[") or text.startswith("[")) and text.endswith("]")):
            return None

        prefix = "#[" if text.startswith("#[") else "["
        body = text[text.find("[") + 1 : -1].strip()
        if body == "":
            return [], prefix, "string"
        parts = [p.strip() for p in body.split(",") if p.strip()]
        return parts, prefix, "string"

    def _parse_numeric_seq_literal(self, value: Any, allow_negative: bool) -> Optional[List[int]]:
        parsed = self._parse_seq_literal(value)
        if parsed is None:
            return None

        parts, _, _ = parsed
        out: List[int] = []
        for p in parts:
            if allow_negative:
                if not re.fullmatch(r"[+-]?\d+", p):
                    return None
            else:
                if not re.fullmatch(r"\d+", p):
                    return None
            out.append(int(p))
        return out

    def _parse_char_token(self, token: str) -> Optional[str]:
        t = token.strip()
        if len(t) == 1:
            return t
        if len(t) == 3 and t[0] == "'" and t[-1] == "'":
            return t[1]
        if len(t) == 3 and t[0] == '"' and t[-1] == '"':
            return t[1]
        return None

    def _parse_char_seq_literal(self, value: Any) -> Optional[List[str]]:
        parsed = self._parse_seq_literal(value)
        if parsed is None:
            return None

        parts, _, _ = parsed
        out: List[str] = []
        for p in parts:
            ch = self._parse_char_token(p)
            if ch is None:
                return None
            out.append(ch)
        return out

    def _render_seq(self, elems: List[Any], prefix: str, storage: str, elem_render) -> Any:
        if storage == "list":
            return elems
        rendered = ", ".join(elem_render(x) for x in elems)
        return f"{prefix}{rendered}]"

    def _mutate_numeric_seq(self, value: Any, allow_negative: bool) -> Any:
        parsed = self._parse_seq_literal(value)
        if parsed is None:
            return value

        parts, prefix, storage = parsed
        ints: List[int] = []
        for p in parts:
            if allow_negative:
                if not re.fullmatch(r"[+-]?\d+", p):
                    return value
            else:
                if not re.fullmatch(r"\d+", p):
                    return value
            ints.append(int(p))

        op = self.rng.randint(0, 4)
        if op == 0 and ints:
            idx = self.rng.randrange(len(ints))
            ints[idx] = self._mutate_int(ints[idx]) if allow_negative else self._mutate_nat(ints[idx])
        elif op == 1:
            ing_kind = "int" if allow_negative else "nat"
            ing = self._pick_ingredient(ing_kind)
            if isinstance(ing, int):
                ints.append(ing if allow_negative else max(0, ing))
            else:
                ints.append(self.rng.randint(-5, 5) if allow_negative else self.rng.randint(0, 5))
        elif op == 2 and len(ints) > 1:
            ints.pop(self.rng.randrange(len(ints)))
        elif op == 3 and ints:
            ints = list(reversed(ints))
        else:
            ints.append(0)

        if not allow_negative:
            ints = [max(0, x) for x in ints]

        return self._render_seq(ints, prefix, storage, lambda x: str(x))

    def _mutate_char_seq(self, value: Any) -> Any:
        parsed = self._parse_seq_literal(value)
        if parsed is None:
            return value

        parts, prefix, storage = parsed
        chars: List[str] = []
        for p in parts:
            ch = self._parse_char_token(p)
            if ch is None:
                return value
            chars.append(ch)

        op = self.rng.randint(0, 4)
        if op == 0 and chars:
            idx = self.rng.randrange(len(chars))
            chars[idx] = self._mutate_char(chars[idx])
        elif op == 1:
            chars.append(self._mutate_char("a"))
        elif op == 2 and len(chars) > 1:
            chars.pop(self.rng.randrange(len(chars)))
        elif op == 3 and chars:
            chars = list(reversed(chars))
        else:
            chars.append(self._mutate_char("z"))

        if storage == "list":
            return chars
        return self._render_seq(chars, prefix, storage, lambda c: f"'{c}'")

    def _mutate_runtime_fallback(self, value: Any) -> Any:
        if isinstance(value, bool):
            return self._mutate_bool(value)
        if isinstance(value, int):
            return self._mutate_int(value)
        if isinstance(value, str):
            return self._mutate_str(value)
        return value

    def _mutate_by_param_type(self, param_type: str, value: Any) -> Any:
        t = self._normalize_param_type(param_type)

        if t == _TYPE_INT:
            if isinstance(value, int):
                return self._mutate_int(value)
            if isinstance(value, str) and re.fullmatch(r"[+-]?\d+", value.strip()):
                return self._mutate_int(int(value.strip()))
            return self._mutate_runtime_fallback(value)

        if t == _TYPE_NAT:
            if isinstance(value, int):
                return self._mutate_nat(value)
            if isinstance(value, str) and re.fullmatch(r"\d+", value.strip()):
                return self._mutate_nat(int(value.strip()))
            return self._mutate_runtime_fallback(value)

        if t == _TYPE_STRING:
            if isinstance(value, str):
                return self._mutate_str(value)
            return self._mutate_str(str(value))

        if t in {_TYPE_LIST_INT, _TYPE_ARRAY_INT}:
            return self._mutate_numeric_seq(value, allow_negative=True)

        if t in {_TYPE_LIST_NAT, _TYPE_ARRAY_NAT}:
            return self._mutate_numeric_seq(value, allow_negative=False)

        if t == _TYPE_LIST_CHAR:
            return self._mutate_char_seq(value)

        return self._mutate_runtime_fallback(value)

    def _mutate_input_once(self, inp: Dict[str, Any]) -> Dict[str, Any]:
        new_inp = deepcopy(inp)
        mutable_params = [p.param_name for p in self.task.signature.parameters if p.param_name in new_inp]
        if not mutable_params:
            return new_inp

        target = self.rng.choice(mutable_params)
        param_type = self.param_types.get(target, "")
        new_inp[target] = self._mutate_by_param_type(param_type, new_inp[target])
        return new_inp

    def mutate_candidates(self, candidates: List[Dict[str, Dict[str, Any]]]) -> List[Dict[str, Dict[str, Any]]]:
        self._bootstrap_ingredients(candidates)

        all_mutated: List[Dict[str, Dict[str, Any]]] = []
        for wrapped in candidates:
            inp = wrapped.get("input", {})
            if not isinstance(inp, dict):
                continue

            generated_for_seed = 0
            attempts = 0
            while (
                generated_for_seed < self.config.max_mutations_per_seed
                and attempts < self.config.max_mutations_per_seed * 4
            ):
                attempts += 1
                new_inp = deepcopy(inp)

                steps = self.rng.randint(1, max(1, self.config.max_multi_step_size))
                for _ in range(steps):
                    new_inp = self._mutate_input_once(new_inp)

                if new_inp != inp:
                    all_mutated.append({"input": new_inp})
                    generated_for_seed += 1
                    for v in new_inp.values():
                        self._fetch_ingredients_from_value(v)

        return dedup_input_wrapped(all_mutated)


def mutate_candidates(task: TaskData, candidates: List[Dict[str, Dict[str, Any]]], max_mutations_per_input: int = 10, seed: int = 42, max_multi_step_size: int = MAX_MULTI_STEP_SIZE, ingredient_prob: float = 0.35) -> List[Dict[str, Dict[str, Any]]]:
    mutator = EvalPlusStyleMutator(
        task,
        MutationConfig(
            max_mutations_per_seed=max_mutations_per_input,
            max_multi_step_size=max_multi_step_size,
            ingredient_prob=ingredient_prob,
            seed=seed,
        ),
    )
    return mutator.mutate_candidates(candidates)
