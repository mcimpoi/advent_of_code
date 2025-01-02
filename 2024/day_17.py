import tqdm
from tqdm.contrib.concurrent import process_map

registers = {
    "A": 0,
    "B": 0,
    "C": 0,
}

reg2 = {}


def read_instructions(fname):
    with open(fname, "r") as f:
        lines = [x.strip() for x in f.readlines()]

    registers["A"] = int(lines[0].split(": ")[1])
    registers["B"] = int(lines[1].split(": ")[1])
    registers["C"] = int(lines[2].split(": ")[1])

    program = [int(x) for x in lines[4].split(": ")[1].split(",")]
    return program


def get_combo(operand):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]
    print("This should not happen")
    return -1


def get_combo2(operand, rega, regb, regc):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return rega
    if operand == 5:
        return regb
    if operand == 6:
        return regc
    print("This should not happen")
    return -1


def run_program(program):
    ip = 0
    outputs = []

    while 0 <= ip < len(program):
        instr = program[ip]
        operand = program[ip + 1]
        # ADV
        if instr == 0:
            numerator = registers["A"]
            denominator = 2 ** get_combo(operand)
            registers["A"] = numerator // denominator
        # BXL
        elif instr == 1:
            registers["B"] ^= operand
        # BST
        elif instr == 2:
            registers["B"] = get_combo(operand) % 8
        # JNZ
        elif instr == 3:
            if registers["A"] != 0:
                ip = operand
                continue
        # BXC
        elif instr == 4:
            registers["B"] = registers["C"] ^ registers["B"]
        # OUT
        elif instr == 5:
            outputs.append(get_combo(operand) % 8)
        # BDV
        elif instr == 6:

            numerator = registers["A"]
            denominator = 2 ** get_combo(operand)
            registers["B"] = numerator // denominator
        # CDV
        elif instr == 7:
            numerator = registers["A"]
            denominator = 2 ** get_combo(operand)
            registers["C"] = numerator // denominator

        ip += 2

    return ",".join([str(x) for x in outputs])


def run_program_parallel(args):
    program, rega, regb, regc = args
    a_val = rega

    ip = 0
    outputs = []

    while 0 <= ip < len(program):
        instr = program[ip]
        operand = program[ip + 1]
        # ADV
        if instr == 0:
            numerator = rega
            denominator = 2 ** get_combo2(operand, rega, regb, regc)
            rega = numerator // denominator
        # BXL
        elif instr == 1:
            regb ^= operand
        # BST
        elif instr == 2:
            regb = get_combo2(operand, rega, regb, regc) % 8
        # JNZ
        elif instr == 3:
            if rega != 0:
                ip = operand
                continue
        # BXC
        elif instr == 4:
            regb = regc ^ regb
        # OUT
        elif instr == 5:
            outputs.append(get_combo2(operand, rega, regb, regc) % 8)
        # BDV
        elif instr == 6:
            numerator = rega
            denominator = 2 ** get_combo2(operand, rega, regb, regc)
            regb = numerator // denominator
        # CDV
        elif instr == 7:
            numerator = rega
            denominator = 2 ** get_combo2(operand, rega, regb, regc)
            regc = numerator // denominator

        ip += 2

    if ",".join([str(x) for x in outputs]) == ",".join([str(x) for x in program]):
        print(a_val)
    idx = -1
    for i in range(len(outputs)):
        if outputs[i] != program[i]:
            idx = i
            break
    if idx >= 10:
        print(a_val, idx, outputs, program)
    if idx == -1:
        print(f"\n======\n{a_val}\n======\n")


def solve_day_17_part_1(fname):
    program = read_instructions(fname)
    return run_program(program)


def solve_day_17_part_2(fname):
    # program = read_instructions(fname)
    program = [2, 4, 1, 1, 7, 5, 4, 5, 3, 0]
    print(program)

    for a_val in range(7263778, 7263778 * 8):
        registers["A"] = a_val
        registers["B"] = 0
        registers["C"] = 0
        res = run_program(program)
        print(res)
        parts = [int(x) for x in res.split(",")]

        if len(parts) < len(program):
            continue

        if len(parts) > len(program):
            print("!")
            break
        if (
            parts[0] == program[0]
            and parts[1] == program[1]
            and parts[2] == program[2]
            and parts[3] == program[3]
            and parts[4] == program[4]
            and parts[5] == program[5]
            and parts[6] == program[6]
            and parts[7] == program[7]
        ):
            print(a_val, oct(a_val), res, "====\n")


def solve_day_17_part_2_parallel(fname):
    program = read_instructions(fname)
    # magic = int("".join([str(x) for x in program[::-1]]), 8) * 10
    magic = 163128703199791
    print(magic)
    chunk_sz = 1000000
    for k in tqdm.tqdm(range(300, 1200)):
        args = [
            (program, x, 0, 0)
            for x in range(magic + chunk_sz * k, magic + chunk_sz * (k + 1))
        ]
        process_map(run_program_parallel, args, chunksize=20000, max_workers=8)


if __name__ == "__main__":
    # solve_day_17_part_2("2024/day_17_large.txt")
    solve_day_17_part_2_parallel("2024/day_17_large.txt")
