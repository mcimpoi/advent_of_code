# https://adventofcode.com/2023/day/3

INPUT_FILE: str = "2023/data/day_03.txt"
INPUT_FILE_SMALL: str = "2023/data/day_03_small.txt"


def parse_line(line: str) -> tuple[list[tuple[int, int, int]], list[tuple[str, int]]]:
    nums, symbols = [], []
    numstr = ""
    start, end = -1, -1
    for i, ch in enumerate(line + "."):
        if ch in "0123456789":
            end = i
            if start == -1:
                start = end
            numstr += ch
        else:
            if numstr != "":
                nums.append((int(numstr), start, end))
                numstr, start, end = "", -1, -1
            if ch == ".":
                numstr, start, end = "", -1, -1
            else:
                symbols.append((ch, i))
    return nums, symbols


def get_nums_and_symbols_coords(
    lines: list[str],
) -> tuple[list[tuple[int, int, int, int]], list[tuple[str, int, int]]]:
    # parsing twice, but the number of lines is small (~ 150)
    all_nums = [
        (value, row, start, end)
        for row, line in enumerate(lines)
        for value, start, end in parse_line(line)[0]
    ]

    all_syms = [
        (sym, row, col)
        for row, line in enumerate(lines)
        for sym, col in parse_line(line)[1]
    ]
    return all_nums, all_syms


def is_adjacent(number_info, symbol_info):
    _, number_row, number_start_col, number_end_col = number_info
    _, symbol_row, symbol_col = symbol_info

    return (
        number_row - 1 <= symbol_row <= number_row + 1
        and number_start_col - 1 <= symbol_col <= number_end_col + 1
    )


def get_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [x.strip() for x in f.readlines()]


def solve_day_03_part_1(input_file: str = INPUT_FILE):
    lines = get_input(input_file)
    nums, symbols = get_nums_and_symbols_coords(lines)
    result = 0
    for num in nums:
        for symbol in symbols:
            if is_adjacent(num, symbol):
                result += num[0]
    return result


def solve_day_03_part_2(input_file: str = INPUT_FILE):
    lines = get_input(input_file)
    numbers, symbols = get_nums_and_symbols_coords(lines)
    result = 0

    for symbol in symbols:
        if symbol[0] != "*":
            continue
        adj_list = []
        for number in numbers:
            if is_adjacent(number, symbol):
                adj_list.append(number[0])
        if len(adj_list) == 2:
            result += adj_list[0] * adj_list[1]

    return result


if __name__ == "__main__":
    print(f"Solution for Part 1 (small): {solve_day_03_part_1(INPUT_FILE_SMALL)}")
    print(f"Solution for Part 2 (small): {solve_day_03_part_2(INPUT_FILE_SMALL)}")

    print(f"Solution for Part 1: {solve_day_03_part_1(INPUT_FILE)}")
    print(f"Solution for Part 2: {solve_day_03_part_2(INPUT_FILE)}")
