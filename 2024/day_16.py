from collections import deque

INFINITY = 10**7

import networkx as nx
import tqdm


def read_grid(fname: str):
    grid = []
    with open(fname, "r") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    return grid


def grid_like(grid, value=0):
    return [[value for _ in range(len(grid[0]))] for _ in range(len(grid))]


def dot_product(vec21, vec22):
    return vec21[0] * vec22[0] + vec21[1] * vec22[1]


def get_cost(path):
    cost = 0
    my_dir = (0, 1)
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]
        direction = (r2 - r1, c2 - c1)
        if dot_product(my_dir, direction) == 0:
            cost += 1001
        else:
            cost += 1
        my_dir = direction
    return cost, len(path)


def solve_day_16_part_1_old(fname: str):
    grid = read_grid(fname)

    G = nx.Graph()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                continue
            if grid[i][j] == "S":
                start = f"{i:03d}-{j:03d}"
            if grid[i][j] == "E":
                end = f"{i:03d}-{j:03d}"
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (
                    0 <= i + dr < len(grid)
                    and 0 <= j + dc < len(grid[0])
                    and grid[i + dr][j + dc] != "#"
                ):
                    G.add_edge(f"{i:03d}-{j:03d}", f"{i + dr:03d}-{j + dc:03d}")

    min_cost = INFINITY
    tested = 0
    for p in tqdm.tqdm(nx.shortest_simple_paths(G, source=start, target=end)):
        crt_cost = get_cost(p)
        if crt_cost < min_cost:
            min_cost = crt_cost
            print(tested, min_cost, print(len(p)))
            tested += 1

    return min_cost


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return i, j
    return -1, -1


def solve_day_16_part_1(fname: str):
    grid = read_grid(fname)

    sr, sc = find_start(grid)

    visited = grid_like(grid, False)

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    q = deque([(sr, sc, (0, 1))])
    costs = grid_like(grid, INFINITY)
    costs[sr][sc] = 0

    while q:
        r, c, mydir = q.popleft()
        if grid[r][c] == "E":
            return costs[r][c]
        for idx_dir, (dr, dc) in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                continue
            if grid[nr][nc] == "#":
                continue
            new_cost = INFINITY
            if mydir == (dr, dc):
                new_cost = costs[r][c] + 1
            elif dot_product(mydir, (dr, dc)) == 0:
                new_cost = costs[r][c] + 1001

            if new_cost < costs[nr][nc]:
                q.append((nr, nc, (dr, dc)))
                costs[nr][nc] = new_cost

    print(costs)

    return -1


def print_costs(grid):
    for r in grid:
        print(" ".join([f"{c: 6d}" if c != INFINITY else "  INF " for c in r]))


def print_costs2(grid):
    for k in range(4):
        for r in grid:
            print(
                " ".join([f"{c[k]: 6d}" if c[k] != INFINITY else "  INF " for c in r])
            )


def solve_day_16_part_1_rec(fname: str):
    grid = read_grid(fname)
    sr, sc = find_start(grid)
    visited = grid_like(grid, False)
    costs = grid_like(grid, (INFINITY, 2, 2))

    costs[sr][sc] = (0, 0, 1)

    q = deque()
    q.append((sr, sc))

    while len(q) > 0:
        crt_r, crt_c = q.popleft()

        crt_cost, crt_dr, crt_dc = costs[crt_r][crt_c]

        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr, nc = crt_r + dr, crt_c + dc

            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                continue
            if grid[nr][nc] == "#":
                continue
            prev_cost, d1r, d1c = costs[nr][nc]
            if dot_product((crt_dr, crt_dc), (dr, dc)) == 0:
                next_cost = crt_cost + 1001
            elif crt_dr == dr and crt_dc == dc:
                next_cost = crt_cost + 1
            if next_cost < prev_cost:
                costs[nr][nc] = (next_cost, dr, dc)
                q.append((nr, nc))

    print_costs(costs)


def solve_day_16_part_2_nx(fname: str, p1_result=0):
    grid = read_grid(fname)

    G = nx.Graph()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                continue
            if grid[i][j] == "S":
                start = (i, j)
            if grid[i][j] == "E":
                end = (i, j)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (
                    0 <= i + dr < len(grid)
                    and 0 <= j + dc < len(grid[0])
                    and grid[i + dr][j + dc] != "#"
                ):
                    G.add_edge((i, j), (i + dr, j + dc))

    print(G.number_of_edges(), G.number_of_nodes())
    min_cost = INFINITY
    tested = 0
    found = 0
    for p in nx.shortest_simple_paths(G, source=start, target=end):
        tested += 1
        if tested % 300 == 0:
            print(tested, ":::", len(p))
        if len(p) < 429:
            continue
        crt_cost, length = get_cost(p)
        if length > 430:
            break
        if tested % 200 == 0:
            print("!! L: Cost:", length, crt_cost)
            print(tested, found)
        if crt_cost == p1_result:
            found += 1
            print(found, tested, length)
            for i in range(length):
                r1, c1 = p[i]
                grid[r1][c1] = "O"

    print(found, tested)

    res = 0
    for r in grid:
        for c in r:
            if c == "O":
                res += 1
    return res


def dijkstra(fname):
    grid = read_grid(fname)
    sr, sc = find_start(grid)

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    dir2idx = {
        (0, 1): 0,
        (0, -1): 1,
        (1, 0): 2,
        (-1, 0): 3,
    }

    q = deque([(sr, sc, (0, 1))])
    costs = [grid_like(grid, INFINITY) for _ in range(4)]
    costs[0][sr][sc] = 0
    while q:
        r, c, mydir = q.popleft()
        if grid[r][c] == "E":
            return costs[0][r][c], costs[1][r][c], costs[2][r][c], costs[3][r][c]

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                continue
            if grid[nr][nc] == "#":
                continue
            new_cost = INFINITY
            if mydir == (dr, dc):
                new_cost = costs[dir2idx[mydir]][r][c] + 1
            elif dot_product(mydir, (dr, dc)) == 0:
                new_cost = costs[dir2idx[mydir]][r][c] + 1001

            if new_cost < costs[dir2idx[mydir]][nr][nc]:
                q.append((nr, nc, (dr, dc)))
                costs[dir2idx[(dr, dc)]][nr][nc] = new_cost

    return -1


def part2(fname):

    grid = read_grid(fname)
    sr, sc = find_start(grid)
    G = nx.DiGraph()

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "#":
                continue
            crt_coord = r + 1j * c
            if cell == "S":
                start = (crt_coord, 1j)
            if cell == "E":
                end = crt_coord
            for direction in (1, -1, 1j, -1j):
                G.add_node((crt_coord, direction))

    for node, direction in G.nodes:
        if (node + direction, direction) in G.nodes:
            G.add_edge((node, direction), (node + direction, direction), weight=1)
            # self + rotation
        G.add_edge((node, direction), (node, direction * 1j), weight=1000)
        G.add_edge((node, direction), (node, direction * -1j), weight=1000)

    for direction in (1, -1, 1j, -1j):
        G.add_edge((end, direction), ("end", None), weight=0)

    for path in nx.all_shortest_paths(
        G, source=start, target=("end", None), weight="weight"
    ):
        for node, _ in path:
            if node == "end":
                continue
            r, c = int(node.real), int(node.imag)
            grid[r][c] = "O"

    res = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "O":
                res += 1

    return res


if __name__ == "__main__":
    # print(solve_day_16_part_2_nx("2024/day_16_large_patch2.txt", p1_result=78428))
    print(part2("2024/day_16_large.txt"))
