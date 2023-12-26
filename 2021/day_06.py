from collections import defaultdict
from io import DEFAULT_BUFFER_SIZE
from typing import List, Tuple

INPUT_FILE = "data/day_06.txt"


def parse_input(input_file: str) -> List[int]:
    with open(input_file, "r") as f:
        lines = [line_.strip() for line_ in f.readlines()]

    return [int(x) for x in lines[0].split(",")]


def solve_day6_p1(input_file: str, num_days: int) -> int:
    nums = parse_input(input_file)

    counts = [0] * 9
    next_counts = [0] * 9

    for nn in nums:
        counts[nn] += 1

    for dd in range(num_days):
        for jj in range(9):
            if jj == 0:
                next_counts[6] += counts[0]
                next_counts[8] += counts[0]
            else:
                next_counts[jj - 1] += counts[jj]
        counts = [x for x in next_counts]
        next_counts = [0] * 9

    return sum(counts)


if __name__ == "__main__":
    print(solve_day6_p1(INPUT_FILE, 80))
    print(solve_day6_p1(INPUT_FILE, 256))
