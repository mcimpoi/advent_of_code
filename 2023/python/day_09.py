from enum import IntEnum


class Direction(IntEnum):
    LEFT = 0
    RIGHT = 1


def get_extrapolated(
    line,
    direction: Direction = Direction.RIGHT,
    index: int = -1,
):
    seq = []
    seq.append(line.copy())
    crt_line = line.copy()
    while not all([v == 0 for v in crt_line]):
        next_line = []
        for n, c in zip(crt_line[1:], crt_line):
            next_line.append(n - c)
        seq.append(next_line)
        crt_line = next_line

    crt_val = 0
    for s in reversed(seq[:-1]):
        next_val = (
            s[index] + crt_val if direction == Direction.RIGHT else s[index] - crt_val
        )
        crt_val = next_val

    return crt_val


def parse_input(input_fname: str) -> list[list[int]]:
    with open(input_fname, "r") as input_file:
        input_str = input_file.read()
    lines = [x.strip() for x in input_str.strip().split("\n")]
    return [[int(x) for x in line.split()] for line in lines]


def solve_day_09_part_01(input_fname: str) -> int:
    lines = parse_input(input_fname)
    return sum([get_extrapolated(line, Direction.RIGHT, -1) for line in lines])


def solve_day_09_part_02(input_fname: str) -> int:
    lines = parse_input(input_fname)
    return sum([get_extrapolated(line, Direction.LEFT, 0) for line in lines])


if __name__ == "__main__":
    print(solve_day_09_part_01("2023/data/day_09.txt"))
    print(solve_day_09_part_02("2023/data/day_09.txt"))
