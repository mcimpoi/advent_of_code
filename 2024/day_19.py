def read_input(fname):
    with open(fname, "r") as f:
        lines = [x.strip() for x in f.readlines()]
        towels = lines[0].split(", ")
        return towels, lines[2:]


cache = {}


def number_of_ways(towels, pattern):
    if len(pattern) == 0:
        return 1
    res = 0
    if pattern in cache:
        return cache[pattern]
    for t in towels:
        if not pattern.startswith(t):
            continue
        res += number_of_ways(towels, pattern[len(t) :])
    cache[pattern] = res
    return res


def possible(towels, pattern):
    tmp_res = False
    if len(pattern) == 0:
        return True
    for t in towels:
        if not pattern.startswith(t):
            continue
        tmp_res = tmp_res or possible(towels, pattern[len(t) :])
    return tmp_res


def solve_day_19_part_1(fname: str) -> int:
    towels, patterns = read_input(fname)
    res = 0
    for pattern in patterns:
        if possible(towels, pattern):
            res += 1
            # print(pattern)
    return res


import tqdm


def solve_day_19_part_2(fname: str) -> int:
    towels, patterns = read_input(fname)
    res = 0
    for pattern in tqdm.tqdm(patterns):
        res += number_of_ways(towels, pattern)
    return res


if __name__ == "__main__":
    print(solve_day_19_part_1("2024/day_19_large.txt"))
    print(solve_day_19_part_2("2024/day_19_large.txt"))
