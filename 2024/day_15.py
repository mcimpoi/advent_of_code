from collections import deque


def get_grid_instr(fname: str) -> list[list[str]]:
    grid = []
    instructions = ""
    with open(fname, "r") as f:
        for line in f.readlines():
            if line.startswith("#"):
                grid.append(list(line.strip()))
            else:
                if len(line) > 0:
                    instructions += line.strip()
    return grid, instructions


def get_robot_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return i, j
    return -1, -1


def print_grid(grid, robot_r=-1, robot_c=-1):
    if robot_r > -1 and robot_c > -1:
        prev_val = grid[robot_r][robot_c]
        grid[robot_r][robot_c] = "@"

    for r in range(len(grid)):
        print("".join(grid[r]))

    if robot_r > -1 and robot_c > -1:
        grid[robot_r][robot_c] = prev_val


def solve_day_15_part_1(fname):
    grid, instructions = get_grid_instr(fname)
    print(len(instructions))
    robot_r, robot_c = get_robot_position(grid)

    instr_dict = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }
    # print_grid(grid)
    grid[robot_r][robot_c] = "."
    for instr in instructions:
        # print(f"\n===\nInstr: {instr}")
        dr, dc = instr_dict[instr]
        if grid[robot_r + dr][robot_c + dc] == "#":
            continue
        if grid[robot_r + dr][robot_c + dc] == ".":
            robot_r += dr
            robot_c += dc
            continue
        if grid[robot_r + dr][robot_c + dc] == "O":
            next_r, next_c = robot_r + dr, robot_c + dc
            while (
                0 < next_r < len(grid)
                and 0 < next_c < len(grid[0])
                and grid[next_r][next_c] != "#"
            ):
                if grid[next_r][next_c] == ".":
                    break
                next_r += dr
                next_c += dc
            if grid[next_r][next_c] == "#":
                continue
            grid[next_r][next_c] = "O"
            robot_r += dr
            robot_c += dc
            grid[robot_r][robot_c] = "."
        # print_grid(grid)

    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "O":
                res += 100 * r + c
    return res


def expand_grid(grid):
    mapping = {
        "#": "##",
        ".": "..",
        "O": "[]",
        "@": "@.",
    }
    new_grid = []
    for row in grid:
        new_row = []
        for col in row:
            new_row += list(mapping[col])
        new_grid.append(new_row)
    return new_grid


# one left and one right can be unified
def masked_move_one_left(grid, robot_r, robot_c):
    masked_grid = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    prev_mask = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for c in range(robot_c - 1, -1, -1):
        if grid[robot_r][c] not in "[]":
            break
        masked_grid[robot_r][c - 1] = grid[robot_r][c]
        prev_mask[robot_r][c] = grid[robot_r][c]
    # print_grid(grid)
    # print_grid(masked_grid)
    return prev_mask, masked_grid


def masked_move_one_right(grid, robot_r, robot_c):
    masked_grid = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    prev_mask = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for c in range(robot_c + 1, len(grid[0])):
        if grid[robot_r][c] not in "[]":
            break
        masked_grid[robot_r][c + 1] = grid[robot_r][c]
        prev_mask[robot_r][c] = grid[robot_r][c]
    # print_grid(grid)
    # print_grid(masked_grid)
    return prev_mask, masked_grid


# one up and one down can be unified.
def masked_move_one_up(grid, robot_r, robot_c):
    masked_grid = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    prev_mask = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]

    q = deque()
    if grid[robot_r - 1][robot_c] == "[":
        q.append((robot_r - 1, robot_c))
        q.append((robot_r - 1, robot_c + 1))
    if grid[robot_r - 1][robot_c] == "]":
        q.append((robot_r - 1, robot_c))
        q.append((robot_r - 1, robot_c - 1))
    while len(q) > 0:
        r, c = q.popleft()
        masked_grid[r - 1][c] = grid[r][c]
        prev_mask[r][c] = grid[r][c]
        if grid[r - 1][c] == "[":
            q.append((r - 1, c))
            q.append((r - 1, c + 1))
        if grid[r - 1][c] == "]":
            q.append((r - 1, c))
            q.append((r - 1, c - 1))

    # print_grid(grid)
    # print_grid(masked_grid)
    return prev_mask, masked_grid


def masked_move_one_down(grid, robot_r, robot_c):
    masked_grid = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    prev_mask = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]

    q = deque()
    if grid[robot_r + 1][robot_c] == "[":
        q.append((robot_r + 1, robot_c))
        q.append((robot_r + 1, robot_c + 1))
    if grid[robot_r + 1][robot_c] == "]":
        q.append((robot_r + 1, robot_c))
        q.append((robot_r + 1, robot_c - 1))
    while len(q) > 0:
        r, c = q.popleft()
        masked_grid[r + 1][c] = grid[r][c]
        prev_mask[r][c] = grid[r][c]
        if grid[r + 1][c] == "[":
            q.append((r + 1, c))
            q.append((r + 1, c + 1))
        if grid[r + 1][c] == "]":
            q.append((r + 1, c))
            q.append((r + 1, c - 1))

    # print_grid(grid)
    # print_grid(masked_grid)
    return prev_mask, masked_grid


def can_move(masked_grid, grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if masked_grid[r][c] in "[]" and grid[r][c] == "#":
                return False
    return True


def make_move(grid, masked_grid, prev_mask):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if prev_mask[r][c] in "[]":
                grid[r][c] = "."
            if masked_grid[r][c] in "[]":
                grid[r][c] = masked_grid[r][c]
    return grid


def solve_day_15_part_2(fname):
    res = 0

    grid, instructions = get_grid_instr(fname)
    print_grid(grid)
    robot_r, robot_c = get_robot_position(grid)
    print(robot_r, robot_c)
    print("==After expand==\n\n")
    grid = expand_grid(grid)

    print(f"Instructions: {len(instructions)}")

    print("=====!\n\n")
    robot_r, robot_c = get_robot_position(grid)

    print(robot_r, robot_c)
    print_grid(grid, robot_r, robot_c)
    print("=====\n\n")

    instr_dict = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }
    # print_grid(grid)
    grid[robot_r][robot_c] = "."
    for instr in instructions:

        dr, dc = instr_dict[instr]
        if grid[robot_r + dr][robot_c + dc] == "#":
            continue
        if grid[robot_r + dr][robot_c + dc] == ".":
            robot_r += dr
            robot_c += dc
            continue
        if grid[robot_r + dr][robot_c + dc] in "[]":
            if instr == "^":
                prev_mask, masked_grid = masked_move_one_up(grid, robot_r, robot_c)
                if can_move(masked_grid, grid):
                    grid = make_move(grid, masked_grid, prev_mask)
                    robot_r += dr
                    robot_c += dc
            if instr == "v":
                prev_mask, masked_grid = masked_move_one_down(grid, robot_r, robot_c)
                if can_move(masked_grid, grid):
                    grid = make_move(grid, masked_grid, prev_mask)
                    robot_r += dr
                    robot_c += dc
            if instr == "<":
                prev_mask, masked_grid = masked_move_one_left(grid, robot_r, robot_c)
                if can_move(masked_grid, grid):
                    grid = make_move(grid, masked_grid, prev_mask)
                    robot_r += dr
                    robot_c += dc
            if instr == ">":
                prev_mask, masked_grid = masked_move_one_right(grid, robot_r, robot_c)
                if can_move(masked_grid, grid):
                    grid = make_move(grid, masked_grid, prev_mask)
                    robot_r += dr
                    robot_c += dc

    print("==***===\n\n")
    print_grid(grid, robot_r, robot_c)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "[":
                res += 100 * r + c
    return res


if __name__ == "__main__":
    print(solve_day_15_part_1("2024/day_15_small.txt"))
    print(solve_day_15_part_2("2024/day_15_small.txt"))
