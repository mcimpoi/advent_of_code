# https://adventofcode.com/2025/day/1
START_DIAL_DEFAULT: int = 50

tiny_input = """ L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def solve_day_01_part1(
    instructions: list[str], start_dial: int = START_DIAL_DEFAULT
) -> int:
    dial = start_dial
    counter = 0
    for line in instructions:
        delta = int(line[1:])
        if line[0] == "L":
            dial -= delta
            dial %= 100
        else:
            dial += delta
            dial %= 100
        if dial == 0:
            counter += 1
    return counter


def solve_day_01_part2(
    instructions: list[str], start_dial: int = START_DIAL_DEFAULT
) -> int:
    dial, counter = start_dial, 0

    for line in instructions:
        delta = int(line[1:])
        prev_dial = dial
        if line[0] == "L":
            dial -= delta
            if dial <= 0:
                counter += abs(dial) // 100 + (1 if prev_dial > 0 else 0)
                dial %= 100
        elif line[0] == "R":
            dial += delta
            counter += dial // 100
            dial %= 100
        else:
            print("error -- input should start with R or L")

    return counter


if __name__ == "__main__":
    instructions = [x.strip() for x in tiny_input.splitlines()]

    part1_solution = solve_day_01_part1(instructions)
    print(f"Part 1 Solution: {part1_solution} | Expected: 3")

    part2_solution = solve_day_01_part2(instructions)
    print(f"Part 2 Solution: {part2_solution} | Expected: 6")
