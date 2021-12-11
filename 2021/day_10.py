from typing import List

INPUT_FILE = "data/day_10.txt"
INPUT_FILE_SMALL = "data/day_10_small.txt"


def parse_input(input_file: str) -> List[str]:
    with open(input_file, "r") as f:
        data = f.readlines()

    return [line.strip() for line in data]


def expected_score(line):
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    expected = {"(": ")", "[": "]", "{": "}", "<": ">"}

    st = []
    for x in line:
        if x in "([{<":
            st.append(x)
        else:
            crt = st.pop()
            if x == expected[crt]:
                continue
            else:
                return scores[x]

    return 0


def score_remaining(line) -> int:
    st = []
    expected = {"(": ")", "[": "]", "{": "}", "<": ">"}
    for ch in line:
        if ch in "([{<":
            st.append(ch)
        else:
            st.pop()

    crt = ""
    while len(st) > 0:
        crt += expected[st.pop()]

    points = {")": 1, "]": 2, "}": 3, ">": 4}

    res = 0
    for ch in crt:
        res *= 5
        res += points[ch]
    return res


def solve_day10_p1(input_file: str) -> int:
    result = 0

    lines = parse_input((input_file))

    for line in lines:
        result += expected_score(line)

    return result


def solve_day10_p2(input_file: str) -> int:
    lines = parse_input((input_file))
    keep = []

    for line in lines:
        if expected_score(line) == 0:
            keep.append(line)

    results = []
    for line in keep:
        results.append(score_remaining(line))

    results.sort()

    return results[len(results) // 2]


if __name__ == "__main__":
    print(solve_day10_p1(INPUT_FILE_SMALL))
    print(solve_day10_p1(INPUT_FILE))
    print(solve_day10_p2(INPUT_FILE_SMALL))
    print(solve_day10_p2(INPUT_FILE))
