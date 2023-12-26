# https://adventofcode.com/2023/day/8
from math import lcm


def get_inputs(fname: str) -> tuple[str, dict[str, list[str]]]:
    with open(fname, "r") as f:
        input_lines = f.read()
    lines = [line.strip() for line in input_lines.strip().split("\n")]
    instructions = lines[0]
    jumps = {}
    for line in lines[2:]:
        jumps[line[0:3]] = [line[7:10], line[12:15]]
    return instructions, jumps


def solve_day_08_part_01(
    input_fname: str,
    start_at: str = "AAA",
    is_end_key: callable = lambda x: x == "ZZZ",
) -> int:
    instructions, jmps = get_inputs(input_fname)
    crt = start_at

    crt_step = 0
    while True:
        step = instructions[crt_step % len(instructions)]
        if step == "L":
            crt = jmps[crt][0]
        else:
            crt = jmps[crt][1]
        # step_cnt += 1
        if is_end_key(crt):
            return crt_step + 1
        crt_step += 1


def solve_day_08_part_02(input_fname: str) -> int:
    instructions, jmps = get_inputs(input_fname)

    start_keys = []
    for key in jmps.keys():
        if key.endswith("A"):
            start_keys.append(key)

    # the input is designed such that length from
    # start to end is the same as length from end to end

    n_steps = []
    for start_key in start_keys:
        n_steps.append(
            solve_day_08_part_01(input_fname, start_key, lambda x: x.endswith("Z"))
        )

    return lcm(*n_steps)


if __name__ == "__main__":
    print(solve_day_08_part_01("2023/data/day_08.txt"))
    print(solve_day_08_part_02("2023/data/day_08.txt"))
