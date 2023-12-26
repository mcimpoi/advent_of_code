# https://adventofcode.com/2023/day/17

from dataclasses import dataclass
from enum import IntEnum
from collections import deque


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


@dataclass
class State:
    up: int = 0
    right: int = 0
    down: int = 0
    left: int = 0


DIRECTIONS = {
    Direction.UP: (-1, 0),
    Direction.RIGHT: (0, 1),
    Direction.DOWN: (1, 0),
    Direction.LEFT: (0, -1),
}


def next_direction(d: Direction) -> Direction:
    if d == Direction.UP:
        return (Direction.UP, Direction.RIGHT, Direction.LEFT)
    elif d == Direction.RIGHT:
        return (Direction.RIGHT, Direction.DOWN, Direction.UP)
    elif d == Direction.DOWN:
        return (Direction.DOWN, Direction.LEFT, Direction.RIGHT)
    elif d == Direction.LEFT:
        return (Direction.LEFT, Direction.UP, Direction.DOWN)


INFINITY = int(1e9)

INPUT_FILE = "2023/data/day_17.txt"
INPUT_FILE_SMALL = "2023/data/day_17_small.txt"


def parse_input(input_file: str) -> list[list[int]]:
    grid = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            grid.append([int(x) for x in list(line.strip())])
    return grid


def solve_day_17_part_01(grid: list[list[int]]) -> int:
    n_rows, n_cols = len(grid), len(grid[0])

    q = deque()
    q.append((0, 0, Direction.RIGHT, 0, 0))
    q.append((0, 0, Direction.DOWN, 0, 0))

    cost = [[INFINITY for _ in range(n_cols)] for _ in range(n_rows)]
    cost[0][0] = 0

    while len(q) > 0:
        crt_r, crt_c, crt_dir, crt_cost, crt_count = q.popleft()

        for next_dir in next_direction(crt_dir):
            if crt_dir == next_dir:
                if crt_count >= 3:
                    continue
                next_count = crt_count + 1
            else:
                next_count = 1
            next_r, next_c = (
                crt_r + DIRECTIONS[next_dir][0],
                crt_c + DIRECTIONS[next_dir][1],
            )
            if 0 <= next_r < n_rows and 0 <= next_c < n_cols:
                new_cost = crt_cost + grid[next_r][next_c]
                if new_cost < cost[next_r][next_c]:
                    cost[next_r][next_c] = new_cost
                    q.append((next_r, next_c, next_dir, new_cost, next_count))

    return cost[n_rows - 1][n_cols - 1]


def solve_day_17_part_02(grid: list[list[int]]) -> int:
    n_rows, n_cols = len(grid), len(grid[0])

    return 0


if __name__ == "__main__":
    grid = parse_input(INPUT_FILE)

    print(f"Part 1: {solve_day_17_part_01(grid)}")
    print(f"Part 2: {solve_day_17_part_02(grid)}")
