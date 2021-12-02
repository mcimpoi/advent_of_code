INPUT_FILE = "data/day_02.txt"


def solve_day2_p1(input_file: str) -> int:
    with open(input_file, "r") as f:
        data = f.readlines()

    start_x, start_y = 0, 0

    for line in data:
        dir, num = line.split()
        if dir == "forward":
            start_x += int(num)
        elif dir == "up":
            start_y -= int(num)
        elif dir == "down":
            start_y += int(num)
        else:
            raise ValueError("This should not happen!")

    return start_x * start_y


def solve_day1_p2(input_file: str) -> int:
    with open(input_file, "r") as f:
        data = f.readlines()

    start_x, start_y, aim = 0, 0, 0

    for line in data:
        dir, num = line.split()
        if dir == "down":
            aim += int(num)
        elif dir == "up":
            aim -= int(num)
        elif dir == "forward":
            start_x += int(num)
            start_y += aim * int(num)
        else:
            raise ValueError("This should not happen!")

    return start_x * start_y


if __name__ == "__main__":
    print(solve_day2_p1(INPUT_FILE))
    print(solve_day1_p2(INPUT_FILE))
