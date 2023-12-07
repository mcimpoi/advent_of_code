# https://adventofcode.com/2023/day/4

from collections import deque


INPUT_FILE: str = "2023/data/day_04.txt"
INPUT_FILE_SMALL: str = "2023/data/day_04_small.txt"


def get_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [x.strip() for x in f.readlines()]


def get_line_score(line: str) -> int:
    parts = line.split(":")[1].split("|")

    winner_numbers = [int(x.strip()) for x in parts[0].split()]
    numbers_on_card = [int(x.strip()) for x in parts[1].split()]

    common = len(set(numbers_on_card).intersection(winner_numbers))
    return 0 if common == 0 else 1 << (common - 1)


def solve_day_04_part_1(input_file: str = INPUT_FILE) -> int:
    lines = get_input(input_file)
    return sum([get_line_score(line) for line in lines])


def get_num_winning_per_line(line: str) -> tuple[int, int]:
    parts = line.split(":")[1].split("|")
    card_num = int(line.split(":")[0].split()[-1])

    winners = [int(x.strip()) for x in parts[0].split()]
    nums_have = [int(x.strip()) for x in parts[1].split()]

    return card_num, len(set(nums_have).intersection(winners))


def solve_day_04_part_2(input_file: str = INPUT_FILE) -> int:
    lines = get_input(input_file)

    card_winners = {
        get_num_winning_per_line(line)[0]: get_num_winning_per_line(line)[1]
        for line in lines
    }

    q = deque(sorted(card_winners.keys()))
    res = len(card_winners)

    while len(q) > 0:
        crt = q.popleft()
        res += card_winners[crt]

        for j in range(crt + 1, crt + card_winners[crt] + 1):
            q.append(j)

    return res


if __name__ == "__main__":
    print(f"Solution for Part 1 (small): {solve_day_04_part_1(INPUT_FILE_SMALL)}")
    print(f"Solution for Part 2 (small): {solve_day_04_part_2(INPUT_FILE_SMALL)}")
    print(f"Solution for Part 1: {solve_day_04_part_1(INPUT_FILE)}")
    print(f"Solution for Part 2: {solve_day_04_part_2(INPUT_FILE)}")
