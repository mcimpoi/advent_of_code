from icecream import ic
from typing import List
import heapq
from collections import defaultdict

INPUT_FILE = "data/day_15.txt"
INPUT_FILE_SMALL = "data/day_15_small.txt"


def parse_input(input_file: str) -> List[List[int]]:
    with open(input_file, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    matrix = []
    for line in lines:
        matrix.append([int(x) for x in line])

    return matrix


def repeat_grid(matrix_in: List[List[int]], multiplier: int) -> List[List[int]]:
    n_rows_in = len(matrix_in)
    n_cols_in = len(matrix_in[0])

    n_rows_out, n_cols_out = n_rows_in * multiplier, n_cols_in * multiplier

    matrix_out = [[0 for _ in range(n_cols_out)] for _ in range(n_rows_out)]

    for rm in range(multiplier):
        for cm in range(multiplier):
            for rr in range(n_rows_in):
                for cc in range(n_cols_in):
                    new_val = matrix_in[rr][cc] + rm + cm
                    while new_val > 9:
                        new_val -= 9
                    matrix_out[rr + n_cols_in * cm][cc + n_rows_in * rm] = new_val

    return matrix_out


def solve_dfs(matrix: List[List[int]]) -> int:
    visited = set()
    pq = []
    nodeCosts = defaultdict(lambda: float("inf"))
    nodeCosts[(0, 0)] = 0
    heapq.heappush(pq, (0, (0, 0)))

    while pq:
        _, node = heapq.heappop(pq)
        visited.add(node)

        for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            adj_node = (node[0] + direction[0], node[1] + direction[1])
            if (
                adj_node[0] < 0
                or adj_node[1] < 0
                or adj_node[0] >= len(matrix)
                or adj_node[1] >= len(matrix[0])
            ):
                continue
            if adj_node in visited:
                continue

            newCost = nodeCosts[node] + matrix[adj_node[0]][adj_node[1]]
            if nodeCosts[adj_node] > newCost:
                nodeCosts[adj_node] = newCost
                heapq.heappush(pq, (newCost, adj_node))

    return nodeCosts[(len(matrix) - 1, len(matrix) - 1)]


def solve(matrix: List[List[int]]) -> int:
    cdist = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    for cc in range(1, n_cols):
        cdist[0][cc] = matrix[0][cc] + cdist[0][cc - 1]
    for rr in range(1, n_rows):
        cdist[rr][0] = matrix[rr][0] + cdist[rr - 1][0]

    for rr in range(1, n_rows):
        for cc in range(1, n_cols):
            cdist[rr][cc] = matrix[rr][cc] + min(cdist[rr - 1][cc], cdist[rr][cc - 1])

    return cdist[n_rows - 1][n_cols - 1]


def solve_day15_p1(input_file: str) -> int:
    matrix = parse_input(input_file)
    return solve(matrix)


def solve_day15_p2(input_file: str) -> int:
    matrix = parse_input(input_file)
    mat2 = repeat_grid(matrix, 5)
    return solve_dfs(mat2)


if __name__ == "__main__":
    ic(solve_day15_p1(INPUT_FILE_SMALL))
    ic(solve_day15_p1(INPUT_FILE))
    ic(solve_day15_p2(INPUT_FILE_SMALL))
    ic(solve_day15_p2(INPUT_FILE))
