from collections import deque, defaultdict


def read_input(file_path):
    grid = []

    with open(file_path, "r") as file:
        lines = file.readlines()
        grid_str = [list(x.strip()) for x in lines]

    for row in grid_str:
        grid.append([int(x) for x in row])

    return grid


def print_grid(grid):
    for row in grid:
        print(" ".join([f"{x:2d}" for x in row]))


def print_grid_mask(grid, mask):
    for rowg, rowm in zip(grid, mask):
        print(
            " ".join([f"{x:2d}" for x in rowg])
            + "|"
            + " ".join([f"{x:2d}" for x in rowm])
        )


def zeros_like(grid):
    return [[0 for _ in row] for row in grid]


def solve_day_10_p1(grid):
    dest = {}
    for r in range(len(grid)):
        dest[r] = {}
        for c in range(len(grid)):
            dest[r][c] = set()

    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] != 9:
                continue
            dest[r][c].add((r, c))
            q = deque()
            q.append((r, c))
            while len(q) > 0:
                crt_r, crt_c = q.pop()
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nr, nc = crt_r + dr, crt_c + dc
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == grid[crt_r][crt_c] - 1
                    ):
                        dest[nr][nc] = dest[nr][nc].union(dest[crt_r][crt_c])
                        q.append((nr, nc))

    res = 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 0:
                res += len(dest[r][c])
    return res


def solve_day_10_p2_dbg(grid):
    dest = {}
    for r in range(len(grid)):
        dest[r] = {}
        for c in range(len(grid)):
            dest[r][c] = 0

    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] != 9:
                continue
            dest[r][c] = 1
            q = deque()
            q.append((r, c))
            while len(q) > 0:
                crt_r, crt_c = q.popleft()
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nr, nc = crt_r + dr, crt_c + dc
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == grid[crt_r][crt_c] - 1
                    ):
                        dest[nr][nc] += dest[crt_r][crt_c]
                        q.append((nr, nc))

    res = 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 0:
                res += dest[r][c]
    return res


def num_paths(grid, x, y):
    if grid[x][y] == 9:
        return 1
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return 0
    res = 0
    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        nr, nc = x + dr, y + dc
        if (
            0 <= nr < len(grid)
            and 0 <= nc < len(grid[0])
            and grid[nr][nc] == grid[x][y] + 1
        ):
            res += num_paths(grid, nr, nc)
    return res


def solve_day_10_p2(grid):
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 0:
                continue
            crt = num_paths(grid, r, c)
            # print(crt)
            total += crt

    print(total)


if __name__ == "__main__":
    data = read_input("2024/day_10_large.txt")
    print(solve_day_10_p2(data))
