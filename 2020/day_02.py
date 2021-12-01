#!/usr/bin/env python3

# Day 2, Part 1: https://adventofcode.com/2020/day/2

from collections import defaultdict
from typing import List, Callable


def solve_D02(password_policy: List[str], validator_func: Callable[[str, int, int, str], int]) -> int:
    num_good: int = 0
    for rule in password_policy:
        parts = rule.split()
        min_, max_ = [int(x) for x in parts[0].split("-")]
        chr_ = parts[1][0]
        pwd_ = parts[2]

        num_good += validator_func(pwd_, min_, max_, chr_)

    return num_good


def validator_part1(pwd: str, min_count: int, max_count: int, letter: str) -> int:
    freq = 0
    for ch in pwd:
        freq += 1 if ch == letter else 0
    return 1 if min_count <= freq <= max_count else 0


def validator_part2(pwd: str, min_count: int, max_count: int, letter: str) -> int:
    return (pwd[min_count - 1] == letter) ^ (pwd[max_count - 1] == letter)


def read_input(fname: str) -> List[str]:
    with open(fname, "r") as f:
        data = f.readlines()
        return [x.strip() for x in data]


if __name__ == "__main__":
    password_db = read_input("data/day2_input.txt")
    print(f"Part  I answer: {solve_D02(password_db, validator_part1)}")
    print(f"Part  II answer: {solve_D02(password_db, validator_part2)}")
