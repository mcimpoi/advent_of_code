from icecream import ic
from collections import defaultdict


INPUT_FILE = "data/day_14.txt"
INPUT_FILE_SMALL = "data/day_14_small.txt"


def solve_by_bigrams(input_file: str, num_steps: int) -> int:
    with open(input_file, "r") as f:
        data = f.readlines()

    pattern = data[0].strip()
    transition_lines = [x.strip() for x in data[2:]]

    transition = {}
    for t_ in transition_lines:
        parts = t_.split(" -> ")
        transition[parts[0]] = parts[1]

    bigram = defaultdict(int)

    for jj in range(1, len(pattern)):
        bigram[pattern[jj - 1 : jj + 1]] += 1

    for _ in range(0, num_steps):
        bigram2_ = defaultdict(int)
        for k, v in bigram.items():
            bigram2_[k[0] + transition[k]] += v
            bigram2_[transition[k] + k[1]] += v
        bigram = bigram2_

    freq_ = defaultdict(int)
    max_freq = 0

    for k in bigram:
        freq_[k[0]] += bigram[k]
        freq_[k[1]] += bigram[k]
        max_freq = max(max_freq, freq_[k[0]])
        max_freq = max(max_freq, freq_[k[1]])

    freq_[pattern[0]] += 1
    freq_[pattern[-1]] += 1

    min_freq = max_freq
    for _, v in freq_.items():
        min_freq = min(min_freq, v)
        max_freq = max(max_freq, v)

    max_freq = max_freq // 2
    min_freq = min_freq // 2

    return max_freq - min_freq


def solve_day14_p1(input_file: str) -> int:
    return solve_by_bigrams(input_file, 10)


def solve_day14_p2(input_file: str) -> int:
    return solve_by_bigrams(input_file, 40)


if __name__ == "__main__":
    ic(solve_day14_p1(INPUT_FILE_SMALL))
    ic(solve_day14_p1(INPUT_FILE))
    ic(solve_day14_p2(INPUT_FILE_SMALL))
    ic(solve_day14_p2(INPUT_FILE))
