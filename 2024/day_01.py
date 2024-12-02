# https://adventofcode.com/2024/day/1

from collections import Counter

SMALL_INPUT: str = """3   4
4   3
2   5
1   3
3   9
3   3"""


def parse_input(input_text: str) -> tuple[list[int], list[int]]:
    nums = [int(x) for x in input_text.split()]
    l1, l2 = nums[0::2], nums[1::2]

    l1.sort()
    l2.sort()
    return l1, l2


def solve_day_01_p1(input_text: str) -> int:
    l1, l2 = parse_input(input_text)
    return sum(abs(x - y) for x, y in zip(l1, l2))


def solve_day_01_p2(input_text: str) -> int:
    l1, l2 = parse_input(input_text)
    d2 = Counter(l2)
    return sum([i * d2[i] for i in l1])


if __name__ == "__main__":
    print(solve_day_01_p1(SMALL_INPUT))  # 11
    print(solve_day_01_p2(SMALL_INPUT))  # 31
