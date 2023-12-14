# https://adventofcode.com/2023/day/11

INPUT_FILE: str = "2023/data/day_11.txt"


def solve_day_11_part_01(input_file: str) -> int:
    return compute_distances2(get_grid(input_file), 1)


def solve_day_11_part_02(input_file: str) -> int:
    return compute_distances2(get_grid(input_file), 999999)


def get_grid(input_file: str) -> list[str]:
    input_lines = ""
    with open(input_file, "r") as input_file:
        input_lines = input_file.read()
    return input_lines.strip().split("\n")


def get_galaxies(grid):
    res = []
    for irow in range(len(grid)):
        for icol in range(len(grid[0])):
            if grid[irow][icol] == "#":
                res.append((irow, icol))
    return res


def get_expanded_cols(grid):
    exp_cols = []
    for c in range(len(grid[0])):
        expand = True
        for r in range(len(grid)):
            if grid[r][c] == "#":
                expand = False
                break
        if expand:
            exp_cols.append(c)
    return exp_cols


def get_expanded_rows(grid):
    exp_rows = []
    for r in range(len(grid)):
        expand = True
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                expand = False
                break
        if expand:
            exp_rows.append(r)
    return exp_rows


def compute_distances2(grid, expansion):
    galaxies = get_galaxies(grid)
    exp_rows = get_expanded_rows(grid)
    exp_cols = get_expanded_cols(grid)
    ret_val = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            crt = abs(galaxies[i][0] - galaxies[j][0]) + abs(
                galaxies[i][1] - galaxies[j][1]
            )
            g_min_row, g_max_row = min(galaxies[i][0], galaxies[j][0]), max(
                galaxies[i][0], galaxies[j][0]
            )
            g_min_col, g_max_col = min(galaxies[i][1], galaxies[j][1]), max(
                galaxies[i][1], galaxies[j][1]
            )
            for r in exp_rows:
                if g_min_row <= r <= g_max_row:
                    crt += expansion
            for c in exp_cols:
                if g_min_col <= c <= g_max_col:
                    crt += expansion
            ret_val += crt
    return ret_val


if __name__ == "__main__":
    print(f"Day 11 Part 01 answer: {solve_day_11_part_01(INPUT_FILE)}")
    print(f"Day 11 Part 02 answer: {solve_day_11_part_02(INPUT_FILE)}")
