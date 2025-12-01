from typing import List, Tuple, Dict

INPUT_FILE = "data/day_02.txt"


def parse_input(input_file: str) -> List[str]:
    lines = []
    with open(input_file, "r") as f:
        lines = [x.strip() for x in f.readlines()]
    return lines


def day_02_part1(input_file: str) -> int:
    p2_lines = parse_input(input_file)

    wins: Tuple[str, ...] = ("A Y", "B Z", "C X")
    draws: Tuple[str, ...] = ("A X", "B Y", "C Z")
    scores: Dict[str, int] = {"X": 1, "Y": 2, "Z": 3}

    res = 0
    for line in p2_lines:
        if line in wins:
            res += 6
        elif line in draws:
            res += 3
        res += scores[line[2]]

    return res


def day_02_part2(input_file: str) -> int:
    p2_lines = parse_input(input_file)

    # Computed pen and paper.
    line_score: Dict[str, int] = {
        "A X": 0 + 3,
        "A Y": 3 + 1,
        "A Z": 6 + 2,
        "B X": 0 + 1,
        "B Y": 3 + 2,
        "B Z": 6 + 3,
        "C X": 0 + 2,
        "C Y": 3 + 3,
        "C Z": 6 + 1,
    }

    return sum([line_score[line] for line in p2_lines])


if __name__ == "__main__":
    print(day_02_part1(INPUT_FILE))
    print(day_02_part2(INPUT_FILE))
