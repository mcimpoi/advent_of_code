# https://adventofcode.com/2024/day/2

SMALL_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def check_report(report: list[int]) -> bool:
    ok = False
    if report[0] > report[1]:
        ok = True
        for r1, r2 in zip(report, report[1:]):
            if r1 <= r2 or r1 - r2 > 3:
                return False
    elif report[0] < report[1]:
        ok = True
        for r1, r2 in zip(report, report[1:]):
            if r1 >= r2 or r2 - r1 > 3:
                return False
    return ok


def solve_day_02_p1(input_text: str) -> int:
    result = 0
    for line in input_text.splitlines():
        report = [int(x) for x in line.split()]
        result += check_report(report)
    return result


def solve_day_02_p2(input_text: str) -> int:
    """The input seems small; brute force is acceptable."""
    result = 0
    for line in input_text.splitlines():
        report = [int(x) for x in line.split()]
        res = False
        for i in range(len(report)):
            res = res or check_report(report[:i] + report[i + 1 :])
        if res:
            result += 1
    return result


if __name__ == "__main__":
    print(solve_day_02_p1(SMALL_INPUT))  # 2
    print(solve_day_02_p2(SMALL_INPUT))  # 4
