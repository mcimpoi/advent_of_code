# https://adventofcode.com/2023/day/16

from collections import deque
from enum import IntEnum

INPUT_FILE: str = "2023/data/day_16.txt"
INPUT_FILE_SMALL: str = "2023/data/day_16_small.txt"


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


DIRECTIONS = {
    Direction.UP: (-1, 0),
    Direction.RIGHT: (0, 1),
    Direction.DOWN: (1, 0),
    Direction.LEFT: (0, -1),
}


def parse_input(input_file: str) -> list:
    with open(input_file) as f:
        text = f.read().strip()
        return [x.strip() for x in text.split("\n")]


def solve_day_16_part_01(
    grid: list,
    start_r: int = 0,
    start_c: int = 0,
    start_dir: Direction = Direction.RIGHT,
) -> int:
    n_rows, n_cols = len(grid), len(grid[0])
    energized = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    visited = {}
    for dir in (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT):
        visited[dir] = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    q = deque()
    q.append(
        (
            start_r,
            start_c,
            start_dir,
        )
    )

    while len(q) > 0:
        crt_r, crt_c, crt_dir = q.popleft()
        energized[crt_r][crt_c] = 1
        visited[crt_dir][crt_r][crt_c] = 1
        if grid[crt_r][crt_c] == ".":
            next_r, next_c = (
                crt_r + DIRECTIONS[crt_dir][0],
                crt_c + DIRECTIONS[crt_dir][1],
            )
            if 0 <= next_r < n_rows and 0 <= next_c < n_cols:
                if not visited[crt_dir][next_r][next_c]:
                    q.append((next_r, next_c, crt_dir))
        elif grid[crt_r][crt_c] == "/":
            if crt_dir == Direction.UP:
                next_dir = Direction.RIGHT
            elif crt_dir == Direction.RIGHT:
                next_dir = Direction.UP
            elif crt_dir == Direction.DOWN:
                next_dir = Direction.LEFT
            else:
                next_dir = Direction.DOWN
            next_r, next_c = (
                crt_r + DIRECTIONS[next_dir][0],
                crt_c + DIRECTIONS[next_dir][1],
            )
            if 0 <= next_r < n_rows and 0 <= next_c < n_cols:
                if not visited[next_dir][next_r][next_c]:
                    q.append((next_r, next_c, next_dir))
        elif grid[crt_r][crt_c] == "\\":
            if crt_dir == Direction.UP:
                next_dir = Direction.LEFT
            elif crt_dir == Direction.RIGHT:
                next_dir = Direction.DOWN
            elif crt_dir == Direction.DOWN:
                next_dir = Direction.RIGHT
            else:
                next_dir = Direction.UP
            next_r, next_c = (
                crt_r + DIRECTIONS[next_dir][0],
                crt_c + DIRECTIONS[next_dir][1],
            )
            if 0 <= next_r < n_rows and 0 <= next_c < n_cols:
                if not visited[next_dir][next_r][next_c]:
                    q.append((next_r, next_c, next_dir))
        elif grid[crt_r][crt_c] == "|":
            if crt_dir in (Direction.UP, Direction.DOWN):
                next_r, next_c = (
                    crt_r + DIRECTIONS[crt_dir][0],
                    crt_c + DIRECTIONS[crt_dir][1],
                )
                if 0 <= next_r < n_rows and 0 <= next_c < n_cols:
                    if not visited[crt_dir][next_r][next_c]:
                        q.append((next_r, next_c, crt_dir))
            else:
                for next_dir in [Direction.UP, Direction.DOWN]:
                    next_r, next_c = (
                        crt_r + DIRECTIONS[next_dir][0],
                        crt_c + DIRECTIONS[next_dir][1],
                    )
                    if 0 <= next_r < n_rows and 0 <= next_c < n_cols:
                        if not visited[next_dir][next_r][next_c]:
                            q.append((next_r, next_c, next_dir))
        elif grid[crt_r][crt_c] == "-":
            if crt_dir in (Direction.LEFT, Direction.RIGHT):
                next_r, next_c = (
                    crt_r + DIRECTIONS[crt_dir][0],
                    crt_c + DIRECTIONS[crt_dir][1],
                )
                if 0 <= next_r < n_rows and 0 <= next_c < n_cols:
                    if not visited[crt_dir][next_r][next_c]:
                        q.append((next_r, next_c, crt_dir))
            else:
                for next_dir in [Direction.LEFT, Direction.RIGHT]:
                    next_r, next_c = (
                        crt_r + DIRECTIONS[next_dir][0],
                        crt_c + DIRECTIONS[next_dir][1],
                    )
                    if 0 <= next_r < n_rows and 0 <= next_c < n_cols:
                        if not visited[next_dir][next_r][next_c]:
                            q.append((next_r, next_c, next_dir))

    return sum([sum(x) for x in energized])


def solve_day_16_part_02(grid: list) -> int:
    max_energized = 0
    n_rows, n_cols = len(grid), len(grid[0])

    for r in range(n_rows):
        sol1 = solve_day_16_part_01(grid, r, 0, Direction.RIGHT)
        max_energized = max(max_energized, sol1)
        sol2 = solve_day_16_part_01(grid, r, n_cols - 1, Direction.LEFT)
        max_energized = max(max_energized, sol2)

    for c in range(n_cols):
        sol1 = solve_day_16_part_01(grid, 0, c, Direction.DOWN)
        max_energized = max(max_energized, sol1)
        sol2 = solve_day_16_part_01(grid, n_rows - 1, c, Direction.UP)
        max_energized = max(max_energized, sol2)

    return max_energized


if __name__ == "__main__":
    grid = parse_input(INPUT_FILE)
    print(f"Part 1: {solve_day_16_part_01(grid)}")
    print(f"Part 2: {solve_day_16_part_02(grid)}")
