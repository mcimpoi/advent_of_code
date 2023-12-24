# https://adventofcode.com/2023/day/18

import numpy as np
import matplotlib.pyplot as plt
from collections import deque

INPUT_FILE: str = "2023/data/day_18.txt"
INPUT_FILE_SMALL: str = "2023/data/day_18_small.txt"


def get_instructions(input_file: str) -> list[tuple[str, str, str]]:
    with open(input_file) as f:
        lines = [line.strip().split() for line in f.readlines()]
        return [(x[0], int(x[1])) for x in lines]


def hex_to_dec(hex_str: str) -> str:
    return int(hex_str, 16)


def get_corrected_instructions(input_file: str) -> list[tuple[str, int]]:
    instr_map = {"0": "R", "1": "D", "2": "L", "3": "U"}
    result: list[tuple[str, int]] = []
    with open(input_file) as f:
        lines = [line.strip().split() for line in f.readlines()]
        for line in lines:
            part = line[-1][1:-1]
            result.append((instr_map[part[-1]], hex_to_dec(part[1:-1])))
    return result


directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}


def print_grid(grid: list[list[int]]) -> None:
    for row in grid:
        for col in row:
            print(col, end="")
        print()


def flood_fill(grid, start, value=2) -> list[list[int]]:
    q = deque()
    q.append(start)

    while len(q) > 0:
        r, c = q.popleft()
        grid[r][c] = value
        for dr, dc in directions.values():
            if grid[r + dr][c + dc] == 0:
                grid[r + dr][c + dc] = value
                q.append((r + dr, c + dc))
    return grid


def count_filled(grid: list[list[int]]) -> int:
    total = 0
    for row in grid:
        for col in row:
            if col != 0:
                total += 1
    return total


def plot_grid(grid: list[list[int]]) -> None:
    plt.imshow(grid)
    plt.show()


def solve_day_18_part_01(
    instructions: list[tuple[str, str, str]],
    offset: tuple[int, int] = (0, 0),
    grid_size: int = 20,
    plot_grid: bool = False,
) -> int:
    res = 0
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    crt_r, crt_c = offset
    grid[crt_r][crt_c] = 1
    for instruction in instructions:
        for _ in range(instruction[1]):
            crt_r, crt_c = (
                crt_r + directions[instruction[0]][0],
                crt_c + directions[instruction[0]][1],
            )
            if crt_r < 0 or crt_c < 0:
                print(crt_r, crt_c)
            try:
                grid[crt_r][crt_c] = 1
            except IndexError:
                print(instruction, crt_r, crt_c)

    grid = flood_fill(grid, (offset[0] + 1, offset[1] + 1))

    if plot_grid:
        plot_grid(grid)
    return count_filled(grid)


def poly_area(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def solve_day_18_part_02(instructions: list[tuple[str, int]]) -> int:
    res = 0
    crt = (0, 0)
    x, y = [0], [0]
    for dir, dist in instructions:
        crt = (
            crt[0] + directions[dir][0] * dist,
            crt[1] + directions[dir][1] * dist,
        )
        x.append(crt[0])
        y.append(crt[1])
    print(crt)
    return poly_area(x, y)


if __name__ == "__main__":
    instructions = get_instructions(INPUT_FILE)
    print(
        f"Part 1: {solve_day_18_part_01(instructions, offset=(400, 200), grid_size=500)}"
    )
    instructions = get_instructions(INPUT_FILE_SMALL)
    print(f"Part 1 small: {solve_day_18_part_01(instructions, grid_size=20)}")
    print(solve_day_18_part_02(instructions))
    corrected_instructions = get_corrected_instructions(INPUT_FILE_SMALL)
    print(f"Part 2: {solve_day_18_part_02(corrected_instructions)}")
