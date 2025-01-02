import networkx as nx
import tqdm


def read_instructions(fname: str) -> list:
    res = []
    with open(fname, "r") as f:
        lines = [x.strip() for x in f.readlines()]
    for line in lines:
        res.append([int(x) for x in line.split(",")])

    return res


def print_grid(grid: list[list[str]]):
    for row in grid:
        print("".join(row))


def solve_day_18_part_1(fname: str, grid_sz: int, n_instr: int) -> int:
    instr = read_instructions(fname)
    res = 0

    grid = [["." for _ in range(grid_sz)] for _ in range(grid_sz)]

    for x, y in instr[:n_instr]:
        grid[y][x] = "#"

    graph = nx.Graph()
    for i in range(grid_sz):
        for j in range(grid_sz):
            if grid[i][j] == "#":
                continue
            graph.add_node((i, j))
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i + dx < grid_sz and 0 <= j + dy < grid_sz:
                    if grid[i + dx][j + dy] != "#":
                        graph.add_edge((i, j), (i + dx, j + dy))
    return nx.shortest_path_length(graph, (0, 0), (grid_sz - 1, grid_sz - 1))


def try_solve(grid_sz, instr, n_instr):
    grid = [["." for _ in range(grid_sz)] for _ in range(grid_sz)]

    for x, y in instr[:n_instr]:
        grid[y][x] = "#"

    # print_grid(grid)

    graph = nx.Graph()
    for i in range(grid_sz):
        for j in range(grid_sz):
            if grid[i][j] == "#":
                continue
            graph.add_node((i, j))
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i + dx < grid_sz and 0 <= j + dy < grid_sz:
                    if grid[i + dx][j + dy] != "#":
                        graph.add_edge((i, j), (i + dx, j + dy))
    return nx.has_path(graph, (0, 0), (grid_sz - 1, grid_sz - 1))


def solve_day_18_part_2(fname: str, grid_sz: int) -> None:
    instr = read_instructions(fname)
    res = 0
    for n_instr in tqdm.tqdm(range(len(instr))):
        if not try_solve(grid_sz, instr, n_instr):
            print(instr[n_instr - 1])
            break


if __name__ == "__main__":
    print(solve_day_18_part_2("2024/day_18_small.txt", 7))
    print(solve_day_18_part_2("2024/day_18_large.txt", 71))
