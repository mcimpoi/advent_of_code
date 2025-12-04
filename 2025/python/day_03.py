tiny_input_03: str = """987654321111111
811111111111119
234234234234278
818181911112111"""


def solve_day_03_part1(grid_str: str) -> int:
    lines = [x.strip() for x in grid_str.splitlines()]

    res = 0
    for line in lines:
        nums = [int(x) for x in line]
        max_val = 11  # 1 1
        for idx1 in range(len(nums)):
            for idx2 in range(idx1 + 1, len(nums)):
                max_val = max(max_val, nums[idx1] * 10 + nums[idx2])
        res += max_val
    return res


def find_next_max_with_index(elems: list[int], start_idx, stop_idx):
    max_val = elems[start_idx]
    max_idx = start_idx
    for idx in range(start_idx + 1, stop_idx):
        if elems[idx] > max_val:
            max_val = elems[idx]
            max_idx = idx
    return max_val, max_idx


def solve_day_03_part2(grid_str: str, num_digits: int = 12) -> int:
    lines = [x.strip() for x in grid_str.splitlines()]
    res = 0
    for line in lines:
        crt_res = 0
        nums = [int(x) for x in line]
        max_idx = len(nums) - num_digits + 1
        start_idx = 0
        for _ in range(num_digits):
            crt_digit, digit_idx = find_next_max_with_index(nums, start_idx, max_idx)
            crt_res *= 10
            crt_res += crt_digit
            start_idx = digit_idx + 1
            max_idx += 1
        res += crt_res

    return res


if __name__ == "__main__":
    part1_solution = solve_day_03_part1(tiny_input_03)
    part2_solves_part1 = solve_day_03_part2(tiny_input_03, num_digits=2)
    print(
        f"Part 1 Solution: {part1_solution} | Expected: 357 | P2 works too {part2_solves_part1 == part1_solution}"
    )

    part2_solution = solve_day_03_part2(tiny_input_03)
    print(f"Part 2 Solution: {part2_solution} | Expected: 3121910778619")
