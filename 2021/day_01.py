INPUT_FILE_P1 = "data/day_01.txt"


def solve_day1_p1(input_file: str) -> int:
    with open(input_file, "r") as f:
        depths = [int(x.strip()) for x in f.readlines()]

    cnt = 0
    for ii in range(1, len(depths)):
        if (depths[ii] > depths[ii - 1]):
            cnt += 1
    return cnt


def solve_day1_p2(input_file: str) -> int:
    with open(input_file, "r") as f:
        depths = [int(x.strip()) for x in f.readlines()]

    cnt = 0

    # sliding[ii] = sliding[ii - 1] - depths[ii - 1] + depths[ii + 2]
    # sliding[ii] > sliding[ii - 1] ==> depths[ii + 2] > depths[ii - 1]
    for ii in range(1, len(depths) - 2):
        if depths[ii + 2] > depths[ii - 1]:
            cnt += 1

    return cnt


if __name__ == "__main__":
    print(solve_day1_p1(INPUT_FILE_P1))
    print(solve_day1_p2(INPUT_FILE_P1))
