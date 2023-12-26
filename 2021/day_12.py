from collections import defaultdict
from typing import List, Dict
from copy import deepcopy


INPUT_FILE = "data/day_12.txt"
INPUT_FILE_SMALL = "data/day_12_larger.txt"
INPUT_FILE_MINI = "data/day_12_mini.txt"
INPUT_FILE_MINI2 = "data/day_12_mini2.txt"

path_count: int = 0
all_paths: List[str] = []
used_two: int = 0


def parse_input(input_file: str):
    with open(input_file, "r") as f:
        lines = [l_.strip() for l_ in f.readlines()]

    graph_ = defaultdict(list)
    for line in lines:
        n1, n2 = line.split("-")
        graph_[n1].append(n2)
        graph_[n2].append(n1)

    return graph_


def count_all_paths(
    graph: Dict[str, List[str]],
    crt_node: str,
    dest_node: str,
    visited: Dict[str, int],
    path: List[str],
) -> None:
    # Bad practice;
    global path_count

    visited[crt_node] = True
    path.append(crt_node)

    if crt_node == dest_node:
        path_count += 1
        all_paths.append([x for x in path])
    else:
        for node in graph[crt_node]:
            if not visited[node] or node.upper() == node:
                count_all_paths(graph, node, dest_node, visited, path)

    path.pop()
    visited[crt_node] = False


def count_all_paths2(
    graph: Dict[str, List[str]],
    crt_node: str,
    dest_node: str,
    visited: Dict[str, int],
    path: List[str],
) -> None:
    # Bad practice;
    global path_count
    global used_two
    global all_paths

    visited[crt_node] += 1
    if crt_node.lower() == crt_node and visited[crt_node] == 2:
        used_two = True
    path.append(crt_node)

    if crt_node == dest_node:
        path_count += 1
        all_paths.append([x for x in path])
    else:
        for node in graph[crt_node]:
            if (
                visited[node] == 0
                or node.upper() == node
                or (node.lower() == node and used_two == False and visited[node] < 2)
            ):
                count_all_paths2(graph, node, dest_node, visited, path)

    path.pop()
    if crt_node.lower() == crt_node and visited[crt_node] == 2:
        used_two = False
    visited[crt_node] -= 1


def solve_day12_p1(input_file: str) -> int:
    graph = parse_input((input_file))

    global path_count
    path_count = 0

    visited = {key: False for key in graph.keys()}

    count_all_paths(graph, crt_node="start", dest_node="end", visited=visited, path=[])

    return path_count


def solve_day12_p2(input_file: str) -> int:
    graph = parse_input((input_file))

    global path_count
    global all_paths
    path_count = 0
    all_paths = []

    visited = {key: 0 for key in graph.keys()}
    visited["start"] = 3

    count_all_paths2(graph, crt_node="start", dest_node="end", visited=visited, path=[])

    return path_count


if __name__ == "__main__":
    print(solve_day12_p1(INPUT_FILE_MINI))
    print(solve_day12_p1(INPUT_FILE_MINI2))
    print(solve_day12_p1(INPUT_FILE_SMALL))
    print(solve_day12_p1(INPUT_FILE))

    print(solve_day12_p2(INPUT_FILE_MINI))
    print(solve_day12_p2(INPUT_FILE_MINI2))
    print(solve_day12_p2(INPUT_FILE_SMALL))
    print(solve_day12_p2(INPUT_FILE))
