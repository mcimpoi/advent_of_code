from collections import deque

INPUT_FILE: str = "2022/data/day_12.txt"
INF: int = 1024


def day_12_part1(input_file: str) -> int:
    with open(input_file, "r") as f:
        grid = [x.strip() for x in f.readlines()]

    n_rows = len(grid)
    n_cols = len(grid[0])

    src_r, src_c = -1, -1
    dst_r, dst_c = -1, -1

    for rr in range(n_rows):
        for cc in range(n_cols):
            if grid[rr][cc] == "S":
                src_r, src_c = rr, cc
            elif grid[rr][cc] == "E":
                dst_r, dst_c = rr, cc

    dist = [[INF for _ in grid[0]] for _ in grid]
    dist[src_r][src_c] = 0

    q = deque()
    q.append((src_r, src_c))

    while len(q) > 0:
        crt_r, crt_c = q.pop()
        crt_dist = dist[crt_r][crt_c]

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (
                0 <= crt_r + dr < n_rows
                and 0 <= crt_c + dc < n_cols
                and (
                    grid[crt_r][crt_c] in "SE"
                    or ord(grid[crt_r + dr][crt_c + dc]) - ord(grid[crt_r][crt_c]) <= 1
                )
            ):
                if crt_dist + 1 < dist[crt_r + dr][crt_c + dc]:
                    dist[crt_r + dr][crt_c + dc] = crt_dist + 1
                    q.append((crt_r + dr, crt_c + dc))

    return dist[dst_r][dst_c]


def bfs(grid: list[str], src_r: int, src_c: int, dst_r: int, dst_c: int) -> int:
    dist = [[INF for _ in grid[0]] for _ in grid]
    dist[src_r][src_c] = 0
    n_rows = len(grid)
    n_cols = len(grid[0])

    q = deque()
    q.append((src_r, src_c))

    while len(q) > 0:
        crt_r, crt_c = q.pop()
        crt_dist = dist[crt_r][crt_c]

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (
                0 <= crt_r + dr < n_rows
                and 0 <= crt_c + dc < n_cols
                and (
                    grid[crt_r][crt_c] in "SE"
                    or ord(grid[crt_r + dr][crt_c + dc]) - ord(grid[crt_r][crt_c]) <= 1
                )
            ):
                if crt_dist + 1 < dist[crt_r + dr][crt_c + dc]:
                    dist[crt_r + dr][crt_c + dc] = crt_dist + 1
                    q.append((crt_r + dr, crt_c + dc))

    return dist[dst_r][dst_c]


def day_12_part2(input_file: str) -> int:
    with open(input_file, "r") as f:
        grid = [x.strip() for x in f.readlines()]

    n_rows = len(grid)
    n_cols = len(grid[0])

    dst_r, dst_c = -1, -1

    for rr in range(n_rows):
        for cc in range(n_cols):
            if grid[rr][cc] == "E":
                dst_r, dst_c = rr, cc

    min_path = INF
    for rr in range(n_rows):
        for cc in range(n_cols):
            if grid[rr][cc] in "Sa":
                min_path = min(min_path, bfs(grid, rr, cc, dst_r, dst_c))
    return min_path


if __name__ == "__main__":
    print(day_12_part1(INPUT_FILE))
    print(day_12_part2(INPUT_FILE))
