def get_input(fname):
    with open(fname, "r") as f:
        lines = [x.strip() for x in f.readlines()]

    locks_str = []
    keys_str = []
    for i in range(len(lines) // 8 + 1):
        if lines[i * 8].startswith("#"):
            locks_str.append(lines[i * 8 + 1 : i * 8 + 6])
        else:
            keys_str.append(lines[i * 8 + 1 : i * 8 + 6])

    locks, keys = [], []
    for lock in locks_str:
        locks.append(parse_grid(lock))
    for key in keys_str:
        keys.append(parse_grid(key))
    return locks, keys


def parse_grid(grid):
    res = [0 for _ in range(len(grid[0]))]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                res[c] += 1
    return res


def fits(lock, key):
    for i in range(len(lock)):
        if lock[i] + key[i] > 5:
            return False
    return True


def solve_day_25_part_1(fname):
    res = 0
    locks, keys = get_input(fname)
    for lock in locks:
        for key in keys:
            if fits(lock, key):
                res += 1
    return res


if __name__ == "__main__":
    print(solve_day_25_part_1("2024/day_25_large.txt"))
