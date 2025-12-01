# https://adventofcode.com/2023/day/6

INPUT_FILE: str = "2023/data/day_06.txt"
INPUT_FILE_SMALL: str = "2023/data/day_06_small.txt"


def parse_input(input_fname: str) -> tuple[list[int], list[int]]:
    with open(input_fname, "r") as input_file:
        input_lines = input_file.read()
        lines = [line.strip() for line in input_lines.strip().split("\n")]

    times = [int(x) for x in lines[0].split(":")[1].split()]
    distances = [int(x) for x in lines[1].split(":")[1].split()]
    return times, distances


def num_ways_to_win(time_, dist):
    res = 0
    for speed in range(time_):
        my_dist = speed * (time_ - speed)
        if my_dist > dist:
            res += 1
    return res


def solve_day_06_part_01(input_fname: str) -> int:
    times, distances = parse_input(input_fname)
    n_ways = [num_ways_to_win(t, d) for t, d in zip(times, distances)]
    p = 1
    for x in n_ways:
        p *= x
    return p


def solve_day_06_part_02(input_fname: str) -> int:
    times, distances = parse_input(input_fname)
    ntime = int("".join([str(t) for t in times]))
    ndist = int("".join([str(d) for d in distances]))
    return num_ways_to_win(ntime, ndist)


if __name__ == "__main__":
    print(solve_day_06_part_01(INPUT_FILE))
    print(solve_day_06_part_02(INPUT_FILE))
