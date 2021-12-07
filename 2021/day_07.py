from collections import defaultdict
from io import DEFAULT_BUFFER_SIZE
from typing import List, Tuple

INPUT_FILE = "data/day_07.txt"
INPUT_FILE_SMALL = "data/day_07_small.txt"


def parse_input(input_file: str) -> List[int]:
    with open(input_file, "r") as f:
        lines = [line_.strip() for line_ in f.readlines()]

    return [int(x) for x in lines[0].split(",")]


def find_median(nums: List[int]) -> int:
    count = len(nums)
    print(count)
    sorted_nums = list(sorted(nums))
    return sorted_nums[count // 2]


def solve_day7_p1(input_file: str) -> int:
    nums = parse_input(input_file)
    median = find_median(nums)
    cost = 0
    for x in nums:
        cost += abs(median - x)
    return cost


def solve_day7_p2(input_file: str) -> int:
    nums = parse_input(input_file)

    min_nums = min(nums)
    max_nums = max(nums)

    min_cost = 1000000000
    for x in range(min_nums, max_nums):
        cost = 0
        for n in nums:
            cost += abs(n - x) * (abs(n - x) + 1) // 2
        if cost < min_cost:
            keep_x = x
            min_cost = cost

    print(keep_x)
    return min_cost


if __name__ == "__main__":
    print(solve_day7_p1(INPUT_FILE_SMALL))
    print(solve_day7_p1(INPUT_FILE))

    print(solve_day7_p2(INPUT_FILE_SMALL))
    print(solve_day7_p2(INPUT_FILE))
