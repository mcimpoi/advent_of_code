# https://adventofcode.com/2023/day/10

from collections import deque
import numpy as np
from skimage.morphology import flood_fill


INPUT_FILE: str = "2023/data/day_10.txt"


def get_grid(input_file: str) -> list[str]:
    input_lines = ""
    with open(input_file, "r") as input_file:
        input_lines = input_file.read()
    return input_lines.strip().split("\n")


def get_start(grid):
    for r, line in enumerate(grid):
        for c, ch in enumerate(line):
            if ch == "S":
                return r, c


directions = {
    "l": (0, -1),
    "r": (0, 1),
    "t": (-1, 0),
    "d": (1, 0),
}

possible = {
    "l": {
        "S": ("-", "F", "L"),
        "-": ("-", "F", "L"),
        "|": (),
        "F": (),
        "L": (),
        "J": ("-", "F", "L"),
        "7": ("-", "F", "L"),
    },
    "r": {
        "S": ("-", "J", "7"),
        "-": ("-", "J", "7"),
        "|": (),
        "F": ("-", "7", "J"),
        "L": ("-", "7", "J"),
        "J": (),
        "7": (),
    },
    "t": {
        "S": ("|", "F", "7"),
        "-": (),
        "|": ("|", "F", "7"),
        "F": (),
        "L": ("|", "7", "F"),
        "J": ("|", "7", "F"),
        "7": (),
    },
    "d": {
        "S": ("|", "L", "J"),
        "-": (),
        "|": ("|", "L", "J"),
        "F": ("|", "L", "J"),
        "L": (),
        "J": (),
        "7": ("|", "L", "J"),
    },
}


def solve_day_10_part_01(input_file: str) -> tuple[int, list[list[int]]]:
    grid = get_grid(input_file)
    n_rows = len(grid)
    n_cols = len(grid[0])

    visited = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    r, c = get_start(grid)
    q = deque()
    q.append((r, c))
    visited[r][c] = 1

    while len(q) > 0:
        crt_r, crt_c = q.popleft()
        crt_ch = grid[crt_r][crt_c]
        for direction in ("l", "r", "t", "d"):
            next_r, next_c = (
                crt_r + directions[direction][0],
                crt_c + directions[direction][1],
            )
            if (
                0 <= next_r < n_rows
                and 0 <= next_c < n_cols
                and visited[next_r][next_c] == 0
            ):
                if grid[next_r][next_c] in possible[direction][crt_ch]:
                    visited[next_r][next_c] = visited[crt_r][crt_c] + 1
                    q.append((next_r, next_c))

    return max([max(x) for x in visited]), visited


def filter_grid(grid, visited):
    new_grid = []
    for r, line in enumerate(grid):
        new_line = ""
        for c, ch in enumerate(line):
            if visited[r][c] > 0:
                # from visual inspection, S is a vertical pipe
                new_line += ch if ch != "S" else "|"
            else:
                new_line += "."
        new_grid.append(new_line)
    return new_grid


def grid2_bitmap(grid3):
    n_rows = len(grid3)
    n_cols = len(grid3[0])
    new_matrix = np.zeros((n_rows * 5, n_cols * 5))
    # TODO: can skip using nunmpy.
    # would probably work with 3x3 matrices as well
    for irow in range(n_rows):
        for icol in range(n_cols):
            if grid3[irow][icol] in ".X":
                new_matrix[irow * 5 + 2, icol * 5 + 2] = 199
            elif grid3[irow][icol] == "-":
                new_matrix[irow * 5 + 2, icol * 5 : icol * 5 + 5] = 255
            elif grid3[irow][icol] == "|":
                new_matrix[irow * 5 : irow * 5 + 5, icol * 5 + 2] = 255
            elif grid3[irow][icol] == "F":
                new_matrix[irow * 5 + 2 : irow * 5 + 5, icol * 5 + 2] = 255
                new_matrix[irow * 5 + 2, icol * 5 + 2 : icol * 5 + 5] = 255
            elif grid3[irow][icol] == "7":
                new_matrix[irow * 5 + 2 : irow * 5 + 5, icol * 5 + 2] = 255
                new_matrix[irow * 5 + 2, icol * 5 : icol * 5 + 2] = 255
            elif grid3[irow][icol] == "L":
                new_matrix[irow * 5 : irow * 5 + 2, icol * 5 + 2] = 255
                new_matrix[irow * 5 + 2, icol * 5 + 2 : icol * 5 + 5] = 255
            elif grid3[irow][icol] == "J":
                new_matrix[irow * 5 : irow * 5 + 2, icol * 5 + 2] = 255
                new_matrix[irow * 5 + 2, icol * 5 : icol * 5 + 3] = 255

    the_matrix = flood_fill(new_matrix, (0, 0), 128)
    # import matplotlib.pyplot as plt

    # plt.figure(figsize=(10, 10))
    # plt.imshow(new_matrix)
    # plt.show()

    # plt.figure(figsize=(10, 10))
    # plt.imshow(the_matrix)
    # plt.show()

    return the_matrix


def solve_day_10_part_02(input_file: str) -> int:
    grid = get_grid(input_file)
    _, visited = solve_day_10_part_01(input_file)

    new_grid = filter_grid(grid, visited)
    bitmap = grid2_bitmap(new_grid)
    n_rows, n_cols = bitmap.shape
    res = 0
    # print(bitmap[350:370, 350:370])
    for r in range(1, n_rows):
        for c in range(1, n_cols):
            if bitmap[r][c] == 199 and bitmap[r - 1][c - 1] == 0:
                res += 1
    return res


if __name__ == "__main__":
    print(f"Day 10 Part 01: {solve_day_10_part_01(INPUT_FILE)[0]}")
    print(f"Day 10 Part 02: {solve_day_10_part_02(INPUT_FILE)}")
