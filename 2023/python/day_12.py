# https://adventofcode.com/2023/day/12


from functools import cache


def get_mask_nums(line: str):
    parts = line.split(" ")
    mask = parts[0]
    nums = [int(x) for x in parts[1].split(",")]
    return mask, nums


@cache
def num_ways(mask, blocks, crt_len):
    # print(mask, idx, blocks, crt_len)
    if mask == "":
        if len(blocks) == 0 and crt_len == 0:
            return 1
        if len(blocks) == 1 and crt_len == blocks[0]:
            return 1
        return 0
    if mask[0] == ".":
        if crt_len == 0:
            return num_ways(mask[1:], blocks, crt_len)
        else:
            if len(blocks) > 0 and crt_len == blocks[0]:
                return num_ways(mask[1:], tuple(blocks[1:]), 0)
            elif crt_len == 0:
                return num_ways(mask[1:], blocks, 0)
            return 0
    if mask[0] == "#":
        if len(blocks) == 0:
            return 0
        if crt_len > blocks[0]:
            return 0
        return num_ways(mask[1:], blocks, crt_len + 1)
    if mask[0] == "?":
        return num_ways("." + mask[1:], blocks, crt_len) + num_ways(
            "#" + mask[1:], blocks, crt_len
        )
    return 0


def solve_day_12_part_01(lines):
    total = 0
    for line in lines:
        mask, nums = get_mask_nums(line)
        total += num_ways(mask, tuple(nums), 0)
    return total


def solve_day_12_part_02(lines):
    total = 0
    for line in lines:
        mask, nums = get_mask_nums(line)
        total += num_ways("?".join([mask] * 5), tuple(nums * 5), 0)
    return total


if __name__ == "__main__":
    INPUT_FILE = "2023/data/day_12.txt"
    print(solve_day_12_part_01(open(INPUT_FILE).read().strip().split("\n")))
    print(solve_day_12_part_02(open(INPUT_FILE).read().strip().split("\n")))
