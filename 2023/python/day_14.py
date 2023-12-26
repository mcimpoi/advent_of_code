def get_grid(input_file):
    with open(input_file, "r") as f:
        lines = f.read()
    return [list(x) for x in lines.strip().split("\n")]


def slide_all(grid):
    n_rows, n_cols = len(grid), len(grid[0])
    # print(n_rows, n_cols)
    for c in range(n_cols):
        r = 0
        while r < n_rows:
            cnt_0 = 0
            start_r = r
            while r < n_rows and grid[r][c] != "#":
                if grid[r][c] == "O":
                    cnt_0 += 1
                r += 1

            for r1 in range(start_r, r):
                if cnt_0 > 0:
                    grid[r1][c] = "O"
                    cnt_0 -= 1
                else:
                    grid[r1][c] = "."
            r += 1

    return grid


def rotate_cw(grid):
    n = len(grid)
    res = [["" for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            res[c][n - r - 1] = grid[r][c]
    return res


def cycle(grid):
    for x in range(4):
        grid = slide_all(grid)
        grid = rotate_cw(grid)
    return grid


def get_total_load(grid):
    load = 0
    for i_row, row in enumerate(reversed(grid)):
        for i_col, ch in enumerate(row):
            if ch == "O":
                load += i_row + 1
    return load


def solve_day_14_part_01(input_file):
    grid = get_grid(input_file)
    grid = slide_all(grid)
    return get_total_load(grid)


def grid_str(grid):
    return "$".join(["".join(r) for r in grid])


def solve_day_14_part_02(input_file):
    grid = get_grid(input_file)
    total_cycles = 1000000000
    states = {}
    states[grid_str(grid)] = 0
    start_cycle = -1
    for n_cycle in range(total_cycles):
        grid = cycle(grid)
        gstr = grid_str(grid)
        if gstr in states:
            start_cycle = states[gstr]
            break
        states[gstr] = n_cycle

    delta = n_cycle - start_cycle
    offset = start_cycle

    num_cycles = (total_cycles - offset) // delta
    remaining_cycles = offset + num_cycles * delta

    search_for = offset + total_cycles - remaining_cycles - 1

    for k, v in states.items():
        if v == search_for:
            restored_grid = [list(x) for x in k.split("$")]
            return get_total_load(restored_grid)
    return -1


if __name__ == "__main__":
    INPUT_FILE = "2023/data/day_14.txt"
    print(solve_day_14_part_01(INPUT_FILE))
    print(solve_day_14_part_02(INPUT_FILE))
