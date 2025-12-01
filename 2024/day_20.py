import networkx as nx
from collections import defaultdict, deque


def get_maze(fname: str):
    with open(fname) as f:
        return [list(line.strip()) for line in f]


def get_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return i, j


def get_end(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "E":
                return i, j


def get_shortest_path(maze, start, end):
    graph = nx.Graph()
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "#":
                continue
            graph.add_node((i, j))
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i + dx < len(maze) and 0 <= j + dy < len(maze[i]):
                    if maze[i + dx][j + dy] != "#":
                        graph.add_edge((i, j), (i + dx, j + dy))

    return nx.shortest_path(graph, start, end)


def get_index(r, c, path):
    for i in range(len(path)):
        if path[i] == (r, c):
            return i
    return -1


import pdb


def solve_day_20_part_1(fname: str, target) -> int:
    maze = get_maze(fname)
    start = get_start(maze)
    end = get_end(maze)
    print(start, end)

    shortest_path = get_shortest_path(maze, start, end)
    path_len = len(shortest_path)
    print(f"{path_len=}")
    hacks = {}

    hacklen = defaultdict(set)
    for start_idx, node in enumerate(shortest_path):
        r, c = node

        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nr1, nc1 = r + dr, c + dc
            if not (0 < nr1 < len(maze) - 1) or not (0 < nc1 < len(maze[0]) - 1):
                continue
            if maze[nr1][nc1] != "#":
                continue
            for dr2, dc2 in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr2, nc2 = nr1 + dr2, nc1 + dc2
                if nr1 == r and nc1 == c:
                    continue
                if not (0 < nr2 < len(maze) - 1) or not (0 < nc2 < len(maze[0]) - 1):
                    continue
                if maze[nr2][nc2] != "#":
                    shortcut_index = get_index(nr2, nc2, shortest_path)
                    if shortcut_index != -1:

                        savings = shortcut_index - start_idx - 2
                        if savings <= 0:
                            continue
                        cheat_id = (nr1, nc1, nr2, nc2)
                        hacks[cheat_id] = savings
                        hacklen[savings].add(cheat_id)
                else:
                    # TODO: check if can connect back to path
                    # seems it's not needed. not sure why.
                    continue

    ret_val = 0
    for k, v in hacklen.items():
        if k >= target:
            ret_val += len(v)
    return ret_val


def solve_day_20_part_2(fname: str, target) -> int:
    maze = get_maze(fname)
    start = get_start(maze)
    end = get_end(maze)
    print(start, end)

    shortest_path = get_shortest_path(maze, start, end)
    path_len = len(shortest_path)
    print(f"{path_len=}")

    hacklen = defaultdict(set)

    for start_idx, (rs, cs) in enumerate(shortest_path):
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            r1, c1 = rs + dr, cs + dc
            if not (0 < r1 < len(maze) - 1) or not (0 < c1 < len(maze[0]) - 1):
                continue
            if maze[r1][c1] != "#":
                continue

            for d1r in range(-20, 20):
                for d1c in range(-20, 20):
                    if abs(d1r) + abs(d1c) > 20:
                        continue
                    nr, nc = r1 + d1r, c1 + d1c
                    if not (0 < nr < len(maze) - 1) or not (0 < nc < len(maze[0]) - 1):
                        continue
                    shortcut_index = get_index(nr, nc, shortest_path)
                    if shortcut_index != -1:
                        savings = shortcut_index - start_idx - 1 - abs(d1r) - abs(d1c)
                        if savings <= 75:
                            continue
                        cheat_id = (r1, c1, nr, nc)
                        hacklen[savings].add(cheat_id)

    ret_val = 0
    for k, v in hacklen.items():

        if k >= target:
            ret_val += len(v)
            print(k, len(v), v)
    return ret_val


def solve_part_2_try_again(fname, threshold):
    # This is what works.
    maze = get_maze(fname)
    start = get_start(maze)
    end = get_end(maze)
    print(start, end)

    shortest_path = get_shortest_path(maze, start, end)
    path_len = len(shortest_path)
    print(f"{path_len=}")

    hacklen = defaultdict(set)

    for start_idx, (rs, cs) in enumerate(shortest_path):
        for end_idx, (re, ce) in enumerate(shortest_path):
            if end_idx <= start_idx + 2:
                continue
            dist = abs(rs - re) + abs(cs - ce)
            if dist > 20:
                continue
            savings = end_idx - start_idx - dist
            if savings <= 0:
                continue
            cheat_id = (rs, cs, re, ce)
            hacklen[savings].add(cheat_id)

    ret_val = 0
    for k, v in hacklen.items():

        if k >= threshold:
            ret_val += len(v)
            # print(k, len(v), v)
    return ret_val


if __name__ == "__main__":
    # print(solve_day_20_part_1("2024/day_20_small.txt", 39))
    # print(solve_day_20_part_1("2024/day_20_large.txt", 100))

    print(solve_part_2_try_again("2024/day_20_large.txt", 100))
