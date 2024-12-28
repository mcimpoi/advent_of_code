def get_input_data(fname: str) -> list[str]:
    with open(fname) as f:
        lines = [x.strip() for x in f.readlines()]

    assigned = {}
    to_compute = {}
    for line in lines:
        if ":" in line:
            key, val = line.split(": ")
            val = int(val)
            assigned[key] = val
        elif "->" in line:
            op, key = line.split(" -> ")
            parts = op.split(" ")
            to_compute[key] = parts
        else:
            pass
    return assigned, to_compute


def solve_generic(fname):
    assigned, to_compute = get_input_data(fname)

    while len(to_compute) > 0:
        for key, parts in to_compute.items():
            if parts[0] in assigned and parts[2] in assigned:
                if parts[1] == "AND":
                    assigned[key] = assigned[parts[0]] & assigned[parts[2]]
                elif parts[1] == "OR":
                    assigned[key] = assigned[parts[0]] | assigned[parts[2]]
                elif parts[1] == "XOR":
                    assigned[key] = assigned[parts[0]] ^ assigned[parts[2]]
                else:
                    pass
                del to_compute[key]
                break
    return assigned


def solve_day_24_part_1(file_name):
    assigned = solve_generic(file_name)
    return to_bin(assigned, "z")


def to_bin(assigned, start):
    res = 0
    for key in sorted(assigned.keys(), reverse=True):
        if key.startswith(start):
            print(key, assigned[key])
            res *= 2
            res += assigned[key]
    return res


def solve_day_24_part_2(file_name):
    assigned, to_compute = get_input_data(file_name)

    for key in sorted(assigned.keys()):
        if key.startswith("x"):
            print(key, assigned[key])

    for key in sorted(assigned.keys()):
        if key.startswith("y"):
            print(key, assigned[key])


if __name__ == "__main__":
    print("Day 24")
    # print("Part 1:", solve_day_24_part_1("2024/day_24_small.txt"))
    print("Part 2:", solve_day_24_part_2("2024/day_24_small.txt"))
