# https://adventofcode.com/2024/day/3
import re

small_input1 = (
    """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
)

small_input2 = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)


def solve_p1(my_input):
    parts = my_input.split("mul")
    keep_parts = [x for x in parts if x.startswith("(") and ")" in x]
    res = 0
    for kp in keep_parts:
        frag = kp[1:].split(")")[0]
        if "," in frag:
            # regex to match "number,number"
            if re.search(r"^\d+,\d+$", frag):
                parts = frag.split(",")
                res += int(parts[0]) * int(parts[1])
    return res


def solve_p2(my_input: str) -> int:
    parts = my_input.split("do()")
    res = 0
    for p in parts:
        p2 = p.split("don't()")
        # ignore everything after don't()
        res += solve_p1(p2[0])

    return res


if __name__ == "__main__":
    print(solve_p1(small_input1))  # 161
    print(solve_p2(small_input2))  # 48
