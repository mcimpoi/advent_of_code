def get_input(input_file):
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    res = []
    for block in range((len(lines) // 4 + 1)):
        btn_a_part = lines[block * 4].split(": ")[1]
        parts = btn_a_part.split(",")
        ax = int(parts[0].split("+")[1])
        ay = int(parts[1].split("+")[1])
        btn_b_part = lines[block * 4 + 1].split(": ")[1]
        parts = btn_b_part.split(",")
        bx = int(parts[0].split("+")[1])
        by = int(parts[1].split("+")[1])
        btn_p_part = lines[block * 4 + 2].split(": ")[1]
        parts = btn_p_part.split(",")
        px = int(parts[0].split("=")[1])
        py = int(parts[1].split("=")[1])
        res.append((ax, ay, bx, by, px, py))
    return res


def solve_day_13_p1(input_file):
    machines = get_input(input_file)
    res = 0

    MIN_COST = 10000
    for machine in machines:
        ax, ay, bx, by, px, py = machine
        min_cost = MIN_COST
        for cnt_a in range(0, 101):
            for cnt_b in range(0, 101):
                if ax * cnt_a + bx * cnt_b == px and ay * cnt_a + by * cnt_b == py:
                    cost = 3 * cnt_a + cnt_b
                    min_cost = min(min_cost, cost)
        if min_cost < MIN_COST:
            res += min_cost

    return res


def solve_day_13_p2(input_file):
    MAGIC = 10000000000000
    machines = get_input(input_file)
    res = 0
    for machine in machines:
        ax, ay, bx, by, px, py = machine
        px, py = px + MAGIC, py + MAGIC

        if ax * by == ay * bx:
            print("!!!!")
            continue
        if (px * ay - py * ax) % (ax * by - ay * bx) != 0:
            continue
        B = (py * ax - px * ay) // (ax * by - ay * bx)
        if (px - B * bx) < 0:
            print("!!**")
            continue
        if (px - B * bx) % ax != 0:
            continue
        A = (px - B * bx) // ax
        if A < 0 or B < 0:
            continue
        res += 3 * A + B
    return res


if __name__ == "__main__":
    print(solve_day_13_p2(input_file="2024/day_13_large.txt"))
