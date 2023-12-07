# https://adventofcode.com/2023/day/5
# TODO: fix bug

from collections import defaultdict

from tqdm import tqdm

INPUT_FILE: str = "2023/data/day_05.txt"
INPUT_FILE_SMALL: str = "2023/data/day_05_small.txt"


def get_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [x.strip() for x in f.readlines()]


def get_seeds(lines: list[str]) -> list[int]:
    for line in lines:
        if line.startswith("seed"):
            return [int(x) for x in line.split(":")[1].strip().split()]
    return []


def get_mappings(lines: list[str]) -> dict[str, list[tuple[int, int, int]]]:
    mappings = defaultdict(list)

    for line in lines:
        if line.endswith("map:"):
            crt_key = line.split()[0].strip()
        elif len(line) > 0:
            dst_start, src_start, range_len = [int(x.strip()) for x in line.split()]
            mappings[crt_key].append((dst_start, src_start, range_len))
    return mappings


def solve_day_05_part_1(input_file: str = INPUT_FILE) -> int:
    lines = get_input(input_file)
    min_val = None
    seeds = get_seeds(lines)
    mappings = get_mappings(lines[1:])

    for crt_seed in seeds:
        crt_value = crt_seed

        for key in (
            "seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location",
        ):
            for dest, src, length in mappings[key]:
                if src <= crt_value < src + length:
                    crt_value = dest + (crt_value - src)
                    break

        if min_val is None:
            min_val = crt_value
        else:
            min_val = min(min_val, crt_value)

    return min_val


def get_from_map(mappings, key, value):
    for dest, src, length in mappings[key]:
        if dest <= value < dest + length:
            return src + value - dest
    return value


# Slow! (inspired from subreddit)
def solve_day_05_part_2(input_file: str = INPUT_FILE) -> int:
    lines = get_input(input_file)
    found = False

    seeds = get_seeds(lines)
    mappings = get_mappings(lines[1:])
    all_keys = all_keys = (
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    )

    for value in tqdm(range(1, solve_day_05_part_1(input_file))):
        start_value = value
        for key in reversed(all_keys):
            value = get_from_map(mappings, key, value)
        # print(key, value)
        for seed, seed_len in zip(seeds[::2], seeds[1::2]):
            if seed <= value <= seed + seed_len - 1:
                print(start_value, "!!! ", value, seed, seed + seed_len - 1)
                found = True
                break
        if found:
            break


if __name__ == "__main__":
    print(f"Solution for Part 1: {solve_day_05_part_1(INPUT_FILE_SMALL)}")
    print(f"Solution for Part 1: {solve_day_05_part_1(INPUT_FILE)}")
