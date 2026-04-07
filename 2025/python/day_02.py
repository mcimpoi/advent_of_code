tiny_input_day_02: str = """ 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def solve_day_02_part1(ranges_str: str) -> int:
    ranges = [x.strip() for x in ranges_str.split(",")]
    intervals = []
    for r in ranges:
        intervals.append([int(x) for x in r.split("-")])

    invalid = []
    for left, right in intervals:
        leftstr = str(left)
        half = len(leftstr) // 2
        leftpart = leftstr[:half]
        if leftpart == "":
            leftpart = "1"
        ileft = int(leftpart)
        invalid_id = int(str(ileft) + str(ileft))
        while invalid_id <= right:
            if invalid_id >= left:
                invalid.append(invalid_id)
            ileft += 1
            invalid_id = int(str(ileft) + str(ileft))

    return sum(invalid)


def solve_day_02_part2(ranges_str: str) -> int:
    ranges = [x.strip() for x in ranges_str.split(",")]
    intervals = []
    for r in ranges:
        intervals.append([int(x) for x in r.split("-")])

    invalid = []
    for left, right in intervals:
        ileft = 1
        invalid_id = 1
        while invalid_id <= right:
            for n_reps in range(2, 20):
                invalid_id = int(str(ileft) * n_reps)
                if invalid_id >= left and invalid_id <= right:
                    invalid.append(invalid_id)
                if invalid_id > right:
                    break
            ileft += 1
            invalid_id = int(str(ileft) + str(ileft))

    return sum(set(invalid))


if __name__ == "__main__":
    part1_solution = solve_day_02_part1(tiny_input_day_02)
    print(f"Part 1 Solution: {part1_solution} | Expected: 1227775554")

    part2_solution = solve_day_02_part2(tiny_input_day_02)
    print(f"Part 2 Solution: {part2_solution} | Expected: 4174379265")
