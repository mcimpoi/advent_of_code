from collections import defaultdict
from io import DEFAULT_BUFFER_SIZE
from typing import List, Tuple, Union, Optional, Dict
from collections import deque

INPUT_FILE: str = "2022/data/day_09.txt"


def parse_input(input_file: str) -> List[Tuple[str, int]]:
    with open(input_file, "r") as f:
        lines = [x.strip() for x in f.readlines()]
    result = []
    for line in lines:
        parts = line.split()
        result.append((parts[0], int(parts[1])))

    return result


def day_09_part1(input_file: str) -> int:
    instructions = parse_input(input_file)
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0

    tail_pos = []
    tail_pos.append(to_str_(tail_x, tail_y))

    delta = {"D": (0, -1), "U": (0, 1), "L": (-1, 0), "R": (1, 0)}

    for direction, distance in instructions:
        # print(f" {direction} {distance} ")
        for step in range(distance):
            head_x, head_y = head_x + delta[direction][0], head_y + delta[direction][1]
            dx, dy = head_x - tail_x, head_y - tail_y
            ux, uy = update_xy(dx, dy)
            tail_x, tail_y = tail_x + ux, tail_y + uy
            tail_pos.append(to_str_(tail_x, tail_y))
            # print(tail_pos)

    return len(set(tail_pos))


def day_09_part2(input_file: str) -> int:
    NUM_KNOTS = 10
    instructions = parse_input(input_file)
    knots = [[0, 0] for _ in range(NUM_KNOTS)]

    tail_pos = []
    tail_pos.append(to_str_(*knots[9]))

    delta = {"D": (0, -1), "U": (0, 1), "L": (-1, 0), "R": (1, 0)}

    LIMIT = 35
    for ii, (direction, distance) in enumerate(instructions[:35]):
        print(f"({ii}) {direction} {distance} ")
        for step in range(distance):
            knots[0][0] += delta[direction][0]
            knots[0][1] += delta[direction][1]
            for knot_id in range(1, NUM_KNOTS):
                dx = knots[knot_id - 1][0] - knots[knot_id][0]
                dy = knots[knot_id - 1][1] - knots[knot_id][1]
                ux, uy = update_xy(dx, dy)
                knots[knot_id][0] += ux
                knots[knot_id][1] += uy
            print(knots)
            tail_pos.append(to_str_(*knots[9]))

    return len(set(tail_pos))


def to_str_(x: int, y: int) -> str:
    return f"{x}_{y}"


def update_xy(dx: int, dy: int) -> Tuple[int, int]:
    if -1 <= dx <= 1 and -1 <= dy <= 1:
        return (0, 0)
    if dx == 0 and dy == 2:
        return (0, 1)
    if dx == 0 and dy == -2:
        return (0, -1)
    if dx == 2 and dy == 0:
        return (1, 0)
    if dx == -2 and dy == 0:
        return (-1, 0)

    if dy == 2 and dx != 0:
        return (dx, 1)
    if dy == -2 and dx != 0:
        return (dx, -1)

    if dx == 2 and dy > 0:
        return (1, 1)
    if dx == 2 and dy < 0:
        return (1, -1)
    if dx == -2 and dy != 0:
        return (-1, 1 if dy > 0 else -1)

    print(f"!!!! {dx} {dy} ")
    return (0, 0)


def update2(dx, dy) -> Tuple[int, int]:
    if -1 <= dx <= 1 and -1 <= dy <= 1:
        return (0, 0)
    return (0, 0)


if __name__ == "__main__":
    print(day_09_part1(INPUT_FILE))
    print(day_09_part2(INPUT_FILE))
