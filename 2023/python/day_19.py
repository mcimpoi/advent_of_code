# https://adventofcode.com/2023/day/19

from dataclasses import dataclass
from enum import Enum
from typing import Optional

INPUT_FILE: str = "2023/data/day_19.txt"
INPUT_FILE_SMALL: str = "2023/data/day_19_small.txt"


class RuleType(Enum):
    GT = 0
    LT = 1
    DECIDE = 2


class RuleResult(Enum):
    REDIRECT = 0
    ACCEPT = 1
    REJECT = 2


@dataclass
class Rule:
    rule_type: RuleType
    rule_threshold: int
    destination: Optional[str]
    rule_result: RuleResult
    rule_field: Optional[str] = None
    str_val: str = ""


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    def __init__(self, s: str) -> None:
        # {x=0,m=1,a=0,s=0}
        parts = s[1:-1].split(",")
        print("Parsing part: parts:", parts)
        for part in parts:
            label, value = part.split("=")
            setattr(self, label, int(value))


def parse_rule(s: str) -> Rule:
    print("Parsing rule: ", s)
    if ":" in s:
        condition, result = s.split(":")
        if "<" in condition or ">" in condition:
            return Rule(
                rule_type=RuleType.LT if "<" in condition else RuleType.GT,
                rule_threshold=int(condition.replace(">", "<").split("<")[1]),
                rule_result=(
                    RuleResult.REDIRECT
                    if result not in "AR"
                    else RuleResult.ACCEPT
                    if result == "A"
                    else RuleResult.REJECT
                ),
                rule_field=s[0],
                destination=result if result not in "AR" else None,
                str_val=s,
            )
    else:
        if s in "AR":
            return Rule(
                rule_type=RuleType.DECIDE,
                rule_threshold=None,
                rule_result=(RuleResult.ACCEPT if s == "A" else RuleResult.REJECT),
                destination=None,
                str_val=s,
            )
        else:
            return Rule(
                rule_type=RuleType.DECIDE,
                rule_threshold=None,
                rule_result=RuleResult.REDIRECT,
                destination=s,
                str_val=s,
            )


def parse_workflow(s: str) -> list[Rule]:
    return [parse_rule(x) for x in s.split(",")]


def get_workflows_and_parts(input_fname: str) -> tuple[dict, list]:
    workflows: dict = {}
    parts: list[Part] = []
    with open(input_fname) as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            if len(line) == 0:
                continue
            if line.startswith("{"):
                parts.append(Part(line))
            else:
                workflows[line.split("{")[0]] = parse_workflow(line.split("{")[1][:-1])

        return workflows, parts


def solve_day_18_part_01(input_fname: str) -> int:
    workflows, parts = get_workflows_and_parts(input_fname)

    decision = [None] * len(parts)
    result = 0
    for idx, part in enumerate(parts):
        workflow = workflows["in"]
        while decision[idx] is None:
            for rule in workflow:
                if rule.rule_type == RuleType.LT:
                    if getattr(part, rule.rule_field) < rule.rule_threshold:
                        if rule.rule_result == RuleResult.REDIRECT:
                            workflow = workflows[rule.destination]
                        else:
                            decision[idx] = rule.rule_result == RuleResult.ACCEPT
                        break
                elif rule.rule_type == RuleType.GT:
                    if getattr(part, rule.rule_field) > rule.rule_threshold:
                        if rule.rule_result == RuleResult.REDIRECT:
                            workflow = workflows[rule.destination]
                        else:
                            decision[idx] = rule.rule_result == RuleResult.ACCEPT
                        break
                elif rule.rule_type == RuleType.DECIDE:
                    if rule.rule_result == RuleResult.REDIRECT:
                        workflow = workflows[rule.destination]
                        break
                    else:
                        decision[idx] = rule.rule_result == RuleResult.ACCEPT
        if decision[idx] == True:
            result += part.x + part.m + part.a + part.s
    return result


if __name__ == "__main__":
    print(solve_day_18_part_01(INPUT_FILE))
