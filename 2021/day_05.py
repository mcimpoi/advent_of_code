from collections import defaultdict
from io import DEFAULT_BUFFER_SIZE
from typing import List, Tuple

INPUT_FILE = "data/day_05.txt"


OFFSET = 100000


def parse_input(input_file: str) -> List[Tuple[int]]:
    with open(input_file, "r") as f:
        lines = [line_.strip() for line_ in f.readlines()]

    coords = []

    for line in lines:
        parts1 = line.split("->")
        x1, y1 = [int(x) for x in parts1[0].split(",")]
        x2, y2 = [int(x) for x in parts1[1].split(",")]
        coords.append((x1, y1, x2, y2))

    return coords


def solve_day5_p1(input_file: str) -> int:
    coords = parse_input(input_file)

    mapping = defaultdict(int)
    cnt = 0

    for line in coords:
        x1, y1, x2, y2 = line
        if (x1 == x2):
            step = 1 if y1 < y2 else -1

            for yy in range(y1, y2 + step, step):
                mapping[x1 * OFFSET + yy] += 1
                if mapping[x1 * OFFSET + yy] == 2:
                    cnt += 1

        if (y1 == y2):
            step = 1 if x1 < x2 else -1
            for xx in range(x1, x2 + step, step):
                mapping[xx * OFFSET + y1] += 1
                if mapping[xx * OFFSET + y1] == 2:
                    cnt += 1

    return cnt


def solve_day5_p2(input_file: str) -> int:
    coords = parse_input(input_file)

    cnt = 0

    mapping = defaultdict(int)
    for line in coords:
        x1, y1, x2, y2 = line

        dx = 0 if x1 == x2 else 1 if x1 < x2 else -1
        dy = 0 if y1 == y2 else 1 if y1 < y2 else -1

        if dx == 0:
            step = 1 if y1 < y2 else -1

            for yy in range(y1, y2 + dy, dy):
                mapping[x1 * OFFSET + yy] += 1
                if mapping[x1 * OFFSET + yy] == 2:
                    cnt += 1

        if dy == 0:
            step = 1 if x1 < x2 else -1
            for xx in range(x1, x2 + dx, dx):
                mapping[xx * OFFSET + y1] += 1
                if mapping[xx * OFFSET + y1] == 2:
                    cnt += 1

        if (dx * dy) != 0:
            for step in range(abs(x1-x2) + 1):
                x, y = x1 + step * dx, y1 + step * dy
                mapping[x * OFFSET + y] += 1
                if mapping[x * OFFSET + y] == 2:
                    cnt += 1

    return cnt


if __name__ == "__main__":
    print(solve_day5_p1(INPUT_FILE))
    print(solve_day5_p2(INPUT_FILE))
