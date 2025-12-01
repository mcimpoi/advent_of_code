INPUT_FILE: str = "2022/data/day_01.txt"


def solve_day1(input_file: str = INPUT_FILE):
    running_sum = 0
    max_sum = 0
    totals = []

    with open(input_file, "r") as f:
        p1_input = f.read()

    for line in p1_input.splitlines():
        if len(line) == 0:
            max_sum = max(max_sum, running_sum)
            totals.append(running_sum)
            running_sum = 0
        else:
            running_sum += int(line)

    print(max_sum)
    totals.sort(reverse=True)
    print(sum(totals[0:3]))


if __name__ == "__main__":
    solve_day1(INPUT_FILE)
