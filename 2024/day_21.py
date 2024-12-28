import networkx as nx
from functools import lru_cache


def get_digit_kbd():
    g = nx.DiGraph()
    for i in range(10):
        g.add_node(i)
    g.add_node("A")

    g.add_edge(7, 8, label=">")
    g.add_edge(8, 9, label=">")
    g.add_edge(4, 5, label=">")
    g.add_edge(5, 6, label=">")
    g.add_edge(1, 2, label=">")
    g.add_edge(2, 3, label=">")
    g.add_edge(0, "A", label=">")

    g.add_edge(8, 7, label="<")
    g.add_edge(9, 8, label="<")
    g.add_edge(5, 4, label="<")
    g.add_edge(6, 5, label="<")
    g.add_edge(2, 1, label="<")
    g.add_edge(3, 2, label="<")
    g.add_edge("A", 0, label="<")

    g.add_edge(1, 4, label="^")
    g.add_edge(2, 5, label="^")
    g.add_edge(3, 6, label="^")
    g.add_edge(4, 7, label="^")
    g.add_edge(5, 8, label="^")
    g.add_edge(6, 9, label="^")
    g.add_edge(0, 2, label="^")
    g.add_edge("A", 3, label="^")

    g.add_edge(4, 1, label="v")
    g.add_edge(5, 2, label="v")
    g.add_edge(6, 3, label="v")
    g.add_edge(7, 4, label="v")
    g.add_edge(8, 5, label="v")
    g.add_edge(9, 6, label="v")
    g.add_edge(2, 0, label="v")
    g.add_edge(3, "A", label="v")

    return g


def get_directional_kbd():
    g = nx.DiGraph()
    for ch in "><^vA":
        g.add_node(ch)

    g.add_edge("<", "v", label=">")
    g.add_edge("v", ">", label=">")
    g.add_edge("^", "A", label=">")

    g.add_edge(">", "v", label="<")
    g.add_edge("v", "<", label="<")
    g.add_edge("A", "^", label="<")

    g.add_edge("v", "^", label="^")
    g.add_edge(">", "A", label="^")

    g.add_edge("^", "v", label="v")
    g.add_edge("A", ">", label="v")

    return g


def node2int(node):
    if node == "A":
        return "A"
    return int(node)


def get_numeric_path_strings(code: str) -> list[str]:
    all_paths = []
    g = get_digit_kbd()
    for path in nx.all_shortest_paths(g, "A", node2int(code[0])):
        crt_path_str = ""
        for n1, n2 in zip(path, path[1:]):
            crt_path_str += g.get_edge_data(n1, n2)["label"]
        all_paths.append(crt_path_str + "A")

    for c1, c2 in zip(code, code[1:]):
        new_segments = []
        for path in nx.all_shortest_paths(g, node2int(c1), node2int(c2)):
            crt_path_str = ""
            for n1, n2 in zip(path, path[1:]):
                crt_path_str += g.get_edge_data(n1, n2)["label"]
            new_segments.append(crt_path_str + "A")
        all_paths = [f"{p1}{p2}" for p1 in all_paths for p2 in new_segments]
    # print(all_paths)
    return all_paths


def get_numeric_path_min(code: str) -> list[str]:
    all_paths = []
    g = get_digit_kbd()
    for path in nx.all_shortest_paths(g, "A", node2int(code[0])):
        crt_path_str = ""
        for n1, n2 in zip(path, path[1:]):
            crt_path_str += g.get_edge_data(n1, n2)["label"]
        all_paths.append(crt_path_str + "A")

    for c1, c2 in zip(code, code[1:]):
        new_segments = []
        for path in nx.all_shortest_paths(g, node2int(c1), node2int(c2)):
            crt_path_str = ""
            for n1, n2 in zip(path, path[1:]):
                crt_path_str += g.get_edge_data(n1, n2)["label"]
            new_segments.append(crt_path_str + "A")
        all_paths = [f"{p1}{p2}" for p1 in all_paths for p2 in new_segments]
    # print(all_paths)
    all_paths.sort()
    min_len = min([len(p) for p in all_paths])
    for p in all_paths:
        if len(p) == min_len:
            return p


def get_directional_path_strings(seq):

    g = get_directional_kbd()

    @lru_cache(None)
    def get_paths(start, end):
        results = []
        for path in nx.all_shortest_paths(g, start, end):
            crt_path_str = ""
            for n1, n2 in zip(path, path[1:]):
                crt_path_str += g.get_edge_data(n1, n2)["label"]
            results.append(crt_path_str + "A")
        return results

    all_paths = get_paths("A", seq[0])

    for c1, c2 in zip(seq, seq[1:]):
        new_segments = get_paths(c1, c2)
        all_paths = [p1 + p2 for p1 in all_paths for p2 in new_segments]

    return all_paths


def solve_day_21_part_1(fname: str) -> int:
    with open(fname) as f:
        codes = [x.strip() for x in f.readlines()]

    res = 0
    for code in codes:
        numeric = get_numeric_path_strings(code)
        robot2 = []
        for num_seq in numeric:
            robot2 += get_directional_path_strings(num_seq)

        print(len(set(robot2)))

        robot3 = []
        for r2 in set(robot2):
            robot3 += get_directional_path_strings(r2)

        print(len(robot3), len(set(robot3)))

        min_len = len(robot3[0])
        shortest = robot3[0]

        for r3 in set(robot3):
            if len(r3) < min_len:
                min_len = len(r3)
                shortest = r3

        print(int(code[:-1]), min_len)
        res += int(code[:-1]) * min_len
    return res


def try_random_stuff(fname: str):
    with open(fname) as f:
        codes = [x.strip() for x in f.readlines()]

    res = 0
    for code in codes:
        print("!", get_numeric_path_strings(code))
        in_seq = get_numeric_path_strings(code)
        directional = get_directional_path_strings(in_seq[0])
        for d in directional:
            print("d: ", len(d), d)
            y = get_directional_path_strings(d)
            print(" y:  ", len(y[0]), y[0])
        print("----")
        break

    print(get_directional_path_strings("A"))

    print(get_directional_path_strings("AA"))

    lessA = get_directional_path_strings("<A")
    for l in lessA:
        print("l: ", len(l), l)
        y = get_directional_path_strings(l)
        print(len(y))
        for yy in y:
            print(" y:  ", len(yy), yy)
            break
        print("----")


if __name__ == "__main__":

    numeric = get_numeric_path_strings("029A")
    directional = get_directional_path_strings(numeric[0])
    print(len(numeric), len(numeric[0]), numeric[0])
    print(len(directional), len(directional[0]), directional[0])

    parts = numeric[0].split("A")
    print(len(parts))
    for part in parts:
        print("part", part)
        dir_parts = get_directional_path_strings(part + "A")
        for dp in dir_parts:
            print(" -", len(dp), dp)

        print("----")

    print(
        len(
            get_directional_path_strings(
                get_directional_path_strings("<A^A>^^AvvvA")[0]
            )[0]
        )
    )
