from collections import defaultdict
from io import DEFAULT_BUFFER_SIZE
from typing import List, Tuple

INPUT_FILE = "data/day_08.txt"
INPUT_FILE_SMALL = "data/day_08_small.txt"


def solve_day8_p1(input_file: str) -> int:
    with open(input_file, "r") as f:
        data = f.readlines()

    count = 0
    for line in data:
        output = line.split("|")[1]
        out_parts = output.split()

        for x in out_parts:
            if len(x) in [2, 3, 4, 7]:
                count += 1
    return count


def solve_day8_p2(input_file: str) -> int:
    with open(input_file, "r") as f:
        data = f.readlines()

    total = 0
    for line in data:
        total += decode(line)

    return total


def decode(line: str) -> int:
    all_signs, output = line.split("|")
    all_signs = ["".join(sorted(x)) for x in all_signs.split()]
    output = ["".join(sorted(x)) for x in output.split()]

    freq = defaultdict(int)
    digits = {}
    for x in all_signs:
        for ch in x:
            freq[ch] += 1

        if len(x) == 2:
            sign_1 = x
            digits[x] = 1
        elif len(x) == 3:
            digits[x] = 7
        elif len(x) == 4:
            sign_4 = x
            digits[x] = 4
        elif len(x) == 7:
            digits[x] = 8

    mid_hor = "*"

    top_left = "*"
    top_right = "*"
    bot_left = "*"
    bot_right = "*"

    for ch in "abcdefg":
        if freq[ch] == 9:
            bot_right = ch
        elif freq[ch] == 6:
            top_left = ch
        elif freq[ch] == 4:
            bot_left = ch

    for ch in sign_1:
        if bot_right != ch:
            top_right = ch

    for ch in sign_4:
        if ch != top_left and ch != top_right and ch != bot_right:
            mid_hor = ch

    for x in all_signs:
        if len(x) == 6:
            if mid_hor not in x:
                digits[x] = 0
            elif bot_left not in x:
                digits[x] = 9
            else:
                digits[x] = 6
        elif len(x) == 5:
            if top_left in x and bot_left not in x:
                digits[x] = 5
            elif top_left not in x and bot_left in x:
                digits[x] = 2
            else:
                digits[x] = 3

    res = 0
    for y in output:
        res *= 10
        res += digits[y]

    return res


if __name__ == "__main__":
    print(solve_day8_p1(INPUT_FILE_SMALL))
    print(solve_day8_p1(INPUT_FILE))
    print(solve_day8_p2(INPUT_FILE_SMALL))
    print(solve_day8_p2(INPUT_FILE))
