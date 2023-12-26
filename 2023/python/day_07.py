# https://adventofcode.com/2023/day/7
from collections import Counter

INPUT_FILE: str = "2023/data/day_07.txt"


def parse_input(input_fname: str) -> list[tuple[str, int]]:
    with open(input_fname, "r") as input_file:
        input_str = input_file.read()
    lines = [x.strip() for x in input_str.strip().split()]
    return [(x, int(y)) for x, y in zip(lines[0::2], lines[1::2])]


def get_rank(hand):
    c = Counter(hand)
    # print(c)
    if len(c) == 1:
        return 10
    if len(c) == 2:
        for k, v in c.items():
            if v == 4:
                return 9
        return 8
    if len(c) == 3:
        for k, v in c.items():
            if v == 3:
                return 7  # three of a kind
        return 6  # two pair
    if len(c) == 4:
        return 5
    return 4


def card_to_number(card):
    cards = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
    res = 0
    for ch in card:
        for idx, c in enumerate(cards):
            if ch == c:
                res *= 16
                res += idx
    return res


def solve_day_07_part_01(input_file: str) -> int:
    game = parse_input(input_file)

    game.sort(key=lambda x: (get_rank(x[0]), -card_to_number(x[0])))
    # print(game)

    res = 0
    for i, hand_ in enumerate(game):
        # print(hand_[1], i + 1, get_rank(hand_[0]), card_to_number(hand_[0]))
        res += hand_[1] * (i + 1)
    return res


def get_rank2(hand):
    max_rank = get_rank(hand)
    for card in ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"):
        tentative_rank = get_rank(hand.replace("J", card))
        max_rank = max(max_rank, tentative_rank)
    return max_rank


def card_to_number2(card):
    cards = ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J")
    res = 0
    for ch in card:
        for idx, c in enumerate(cards):
            if ch == c:
                res *= 16
                res += idx
    return res


def solve_day_07_part_02(input_file: str) -> int:
    game = parse_input(input_file)

    game.sort(key=lambda x: (get_rank2(x[0]), -card_to_number2(x[0])))
    # print(game)

    res = 0
    for i, hand_ in enumerate(game):
        # print(hand_[1], i + 1, get_rank(hand_[0]), card_to_number(hand_[0]))
        res += hand_[1] * (i + 1)
    return res


if __name__ == "__main__":
    print(solve_day_07_part_01(INPUT_FILE))
    print(solve_day_07_part_02(INPUT_FILE))
