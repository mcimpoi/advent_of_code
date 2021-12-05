from collections import defaultdict

INPUT_FILE = "data/day_03.txt"


def solve_day3_p1(input_file: str) -> int:
    with open(input_file, "r") as f:
        lines = [line_.strip() for line_ in f.readlines()]

    nbits = len(lines[0])
    counts = [0] * nbits

    for line in lines:
        for ii in range(nbits):
            counts[ii] += (line[ii] == "1")

    g = 0
    e = 0

    for ii in range(nbits):
        crtBit = counts[ii] > len(lines) / 2
        g *= 2
        g += crtBit

        e *= 2
        e += (1 - crtBit)

    return g * e


def solve_day3_p2(input_file: str) -> int:
    with open(input_file, "r") as f:
        lines = [line_.strip() for line_ in f.readlines()]

    nbits = len(lines[0])
    counts = [0] * nbits

    orig_lines = [x for x in lines]

    for ii in range(nbits):
        count1 = 0

        if len(lines) == 1:
            break

        for line in lines:
            if line[ii] == '1':
                count1 += 1

        lines = [x for x in lines if x[ii] == "1"] if count1 >= len(
            lines) / 2 else [x for x in lines if x[ii] == "0"]

    res_o = 0
    for x in range(nbits):
        res_o *= 2
        res_o += (lines[0][x] == "1")

    print(res_o)

    lines = [x for x in orig_lines]
    for ii in range(nbits):
        count1 = 0

        if len(lines) == 1:
            break

        for line in lines:
            if line[ii] == '1':
                count1 += 1

        lines = [x for x in lines if x[ii] == "1"] if count1 < len(
            lines) / 2 else [x for x in lines if x[ii] == "0"]

        print(f"Step: {ii}")
        print("\n".join(lines))

    res_co = 0
    for x in range(nbits):
        res_co *= 2
        res_co += lines[0][x] == "1"

    print(f"{res_co}\n====\n")
    return res_o * res_co


if __name__ == "__main__":
    print(solve_day3_p1(INPUT_FILE))
    print(solve_day3_p2(INPUT_FILE))
