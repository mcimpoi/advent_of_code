from icecream import ic
from typing import List, Tuple
from copy import deepcopy


INPUT_FILE = "data/day_13.txt"
INPUT_FILE_SMALL = "data/day_13_small.txt"


def parse_input(input_file: str) -> Tuple[List, List]:
    with open(input_file, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    coords = []
    folds = []
    for line in lines:
        if len(line) == 0:
            continue
        elif line.startswith("fold"):
            parts = line.split()
            folds.append(parts[-1].split("="))
        else:
            coords.append([int(x) for x in line.split(",")])

    return coords, folds


def do_folding(input_file: str, n_steps: int) -> List[List[int]]:
    coords, folds = parse_input(input_file)

    max_x = 0
    max_y = 0

    for x, y in coords:
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    for ii, (axis, size) in enumerate(folds):
        if ii == n_steps:
            break
        dim = int(size)

        if axis == "y":

            for ii in range(len(coords)):

                if coords[ii][1] >= dim:
                    coords[ii][1] = 2 * dim - coords[ii][1]
            max_y = dim
        else:
            for ii in range(len(coords)):

                if coords[ii][0] >= dim:
                    coords[ii][0] = 2 * dim - coords[ii][0]
            max_x = dim

    return coords, max_x, max_y


def solve_day13_p1(input_file: str) -> int:

    coords_, _, _ = do_folding(input_file, 1)
    res = []
    for x, y in coords_:
        res.append(f"{x},{y}")

    return len(set(res))


def solve_day13_p2(input_file: str) -> None:
    coords_, max_x, max_y = do_folding(input_file, -1)

    my_grid = [["." for _ in range(max_x)] for _ in range(max_y + 1)]

    for x, y in coords_:
        my_grid[y][x] = "#"

    for y in range(max_y):
        line = "".join(my_grid[y])
        ic(line)


if __name__ == "__main__":
    ic(solve_day13_p1(INPUT_FILE_SMALL))
    ic(solve_day13_p1(INPUT_FILE))

    solve_day13_p2(INPUT_FILE_SMALL)
    solve_day13_p2(INPUT_FILE)
