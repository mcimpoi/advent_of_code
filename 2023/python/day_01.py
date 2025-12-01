# https://adventofcode.com/2023/day/1

INPUT_FILE: str = "2023/data/day_01.txt"

DIGITS_AS_TEXT = (
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)


def get_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [x.strip() for x in f.readlines()]


def solve_day_01_part_1(input_file: str = INPUT_FILE):
    lines = get_input(input_file)

    result: int = 0
    for line in lines:
        digits = [int(x) for x in line if x in "0123456789"]
        result += digits[0] * 10 + digits[-1]

    return result


def solve_day_01_part_2(input_file: str = INPUT_FILE):
    lines = get_input(input_file)

    res = 0
    for line in lines:
        digits = []
        for i in range(len(line)):
            if line[i] in "0123456789":
                digits.append(int(line[i]))
            else:
                for j, wd in enumerate(DIGITS_AS_TEXT):
                    if line[i:].startswith(wd):
                        digits.append(j + 1)
        res += digits[0] * 10 + digits[-1]

    return res


if __name__ == "__main__":
    print(f"Solution for Part 1: {solve_day_01_part_1(INPUT_FILE)}")
    print(f"Solution for Part 2: {solve_day_01_part_2(INPUT_FILE)}")
