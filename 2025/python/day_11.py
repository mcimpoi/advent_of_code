import networkx as nx
import os
import tqdm

def solve_day_11_part_1(fname: str) -> int:
    with open(fname, "r") as f:
        lines = [x.strip() for x in f.readlines()]
    dg = nx.DiGraph()
    for i, line in enumerate(lines):
        src, dest_part = line.split(":")
        dests = [x.strip() for x in dest_part.split(" ") if len(x) > 1]
        for dest in dests:
            dg.add_edge(src, dest)

    return len(list(nx.all_simple_paths(dg, "you", "out")))

def solve_day_11_part_2(fname: str) -> int:
    with open(fname, "r") as f:
        lines = [x.strip() for x in f.readlines()]
    dg = nx.DiGraph()
    for i, line in enumerate(lines):
        src, dest_part = line.split(":")
        dests = [x.strip() for x in dest_part.split(" ") if len(x) > 1]
        for dest in dests:
            dg.add_edge(src, dest)

    res = 0
    idx = 0
    import pdb

    for path in nx.all_simple_paths(dg, "svr", "out"):

        idx += 1
        if idx % 100 == 0:
            pdb.set_trace()
            print(f"Processed {idx} paths, current count {res}")
        print()
        if "dac" in path and "fft" in path:
            res += 1
    return res


if __name__ == "__main__":
    print(solve_day_11_part_1(os.path.expanduser("~/day_11.txt")))
    print(solve_day_11_part_2(os.path.expanduser("~/day_11.txt")))
    