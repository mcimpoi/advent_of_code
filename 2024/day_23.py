from collections import defaultdict


def read_input(fname):
    with open(fname, "r") as f:
        pairs = [x.strip().split("-") for x in f.readlines()]

    return pairs


def solve_day_23_part_1(fname: str) -> int:
    pairs = read_input(fname)
    neigh = defaultdict(list)
    for pair in pairs:
        neigh[pair[0]].append(pair[1])
        neigh[pair[1]].append(pair[0])

    res = set()
    for key1 in neigh.keys():
        for key2 in neigh[key1]:
            for key3 in neigh[key2]:
                if key3 in neigh[key1]:
                    if (
                        key1.startswith("t")
                        or key2.startswith("t")
                        or key3.startswith("t")
                    ):
                        s1, s2, s3 = sorted([key1, key2, key3])
                        res.add((s1, s2, s3))
    return len(res), res


def solve_day_23_part_2_old(fname: str) -> int:
    pairs = read_input(fname)
    neigh = defaultdict(list)

    nodes = set()
    for pair in pairs:
        neigh[pair[0]].append(pair[1])
        neigh[pair[1]].append(pair[0])
        nodes.add(pair[0])
        nodes.add(pair[1])

    edges = set()
    with open(fname, "r") as f:
        edges = set([x.strip() for x in f.readlines()])

    sets_of_3 = set()
    for key1 in neigh.keys():
        for key2 in neigh[key1]:
            for key3 in neigh[key2]:
                if key3 in neigh[key1]:

                    s1, s2, s3 = sorted([key1, key2, key3])
                    sets_of_3.add((s1, s2, s3))

    solutions = defaultdict(set)
    max_sz = 3
    for s1, s2, s3 in sets_of_3:
        crt_set = set([s1, s2, s3])
        prev_sz = 3
        crt_sz = -1

        while True:
            for node in nodes:
                if node in crt_set:
                    continue
                all_neighbors = True
                for nc in crt_set:
                    if node not in neigh[nc]:
                        all_neighbors = False
                        break
                if all_neighbors:
                    crt_set.add(node)
                    crt_sz = len(crt_set)
                    break
            if prev_sz == crt_sz:
                break
            prev_sz = crt_sz

        if crt_sz >= max_sz:
            max_sz = crt_sz
            solutions[max_sz].add(",".join(sorted(crt_set)))
            # print(max_sz, solutions[max_sz])

    print(max_sz, solutions[max_sz])
    return max_sz, solutions[max_sz]


import networkx as nx


def solve_day_23_part_2(fname: str) -> int:
    pairs = read_input(fname)
    g = nx.Graph()
    nodes = set()
    for pair in pairs:
        nodes.add(pair[0])
        nodes.add(pair[1])

    g.nodes = nodes
    for pair in pairs:
        g.add_edge(pair[0], pair[1])

    for clq in list(nx.find_cliques(g)):
        if len(clq) < 10:
            continue
        print(",".join(sorted(clq)), len(clq))


if __name__ == "__main__":
    print(solve_day_23_part_1("2024/day_23_large.txt")[0])
    solve_day_23_part_2_old("2024/day_23_large.txt")
