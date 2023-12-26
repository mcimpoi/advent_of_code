from typing import List
from copy import deepcopy


INPUT_FILE = "data/day_11.txt"
INPUT_FILE_SMALL = "data/day_11_small.txt"


GRID_DIM = 10


def parse_input(input_file: str) -> List[List[int]]:
    with open(input_file, "r") as f:
        data = f.readlines()

    result = []
    for line in data:
        result.append([int(v) for v in line.strip()])
    return result


def do_step(grid) -> int:
    flashed = [[0 for _ in range(GRID_DIM)] for _ in range(GRID_DIM)]
    out_grid = deepcopy(grid)

    res = 0

    flash = False

    for rr in range(GRID_DIM):
        for cc in range(GRID_DIM):
            out_grid[rr][cc] += 1
            if out_grid[rr][cc] > 9 and flashed[rr][cc] == 0:
                flashed[rr][cc] = 1
                flash = True

    while flash:
        flash = False
        for rr in range(GRID_DIM):
            for cc in range(GRID_DIM):
                if flashed[rr][cc] == 1:
                    flashed[rr][cc] = 2
                    res += 1

                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dc == 0 and dr == 0:
                                continue
                            if (
                                0 <= rr + dr < GRID_DIM
                                and 0 <= cc + dc < GRID_DIM
                                and flashed[rr + dr][cc + dc] == 0
                            ):
                                out_grid[rr + dr][cc + dc] += 1
                                if out_grid[rr + dr][cc + dc] > 9:
                                    flashed[rr + dr][cc + dc] = 1
                                    flash = True

    for rr in range(GRID_DIM):
        for cc in range(GRID_DIM):
            if out_grid[rr][cc] > 9:
                out_grid[rr][cc] = 0

    return out_grid, res


def print_grid(grid) -> None:
    for rr in range(GRID_DIM):
        print(" ".join(str(x) for x in grid[rr]))


def solve_day11_p1(input_file: str) -> int:
    grid = parse_input((input_file))

    result = 0
    # print_grid(grid)
    for step in range(100):
        grid, flashes = do_step(grid)
        result += flashes

    # print("===\n")
    # print_grid(grid)

    return result


def solve_day11_p2(input_file: str) -> int:
    grid = parse_input((input_file))

    # print_grid(grid)
    for step in range(1, 500):
        grid, flashes = do_step(grid)
        ok = True
        for rr in range(GRID_DIM):
            for cc in range(GRID_DIM):
                if grid[rr][cc] != 0:
                    ok = False
                    break
        if ok:
            return step
    return 0


if __name__ == "__main__":
    print(solve_day11_p1(INPUT_FILE_SMALL))
    print(solve_day11_p1(INPUT_FILE))
    print(solve_day11_p2(INPUT_FILE_SMALL))
    print(solve_day11_p2(INPUT_FILE))
