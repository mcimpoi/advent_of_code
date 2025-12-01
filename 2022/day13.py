INPUT_FILE: str = "2022/data/day_13.txt"


def parse_inputs(input_file: str) -> list:
    with open(input_file, "r") as f:
        data = [x.strip() for x in f.readlines() if len(x.strip()) > 0]

    return [eval(x) for x in data]


def day_13_part1(input_file: str) -> int:
    pairs = parse_inputs(input_file)

    # print(in_order(eval("[7, 7]"), eval("[7]")))

    total = 0
    for ii in range(len(pairs) // 2):
        left = pairs[2 * ii]
        right = pairs[2 * ii + 1]
        res = in_order(left, right)
        if res:
            total += ii + 1

    return total


def in_order(left: list, right: list) -> bool:
    if left is None and right is None:
        return True
    if left is None and right is not None:
        return True
    if len(left) == 0 and len(right) > 0:
        return True
    if len(left) > 0 and len(right) == 0:
        return False
    if isinstance(left[0], int) and isinstance(right[0], int):
        if left[0] < right[0]:
            return True
        elif left[0] > right[0]:
            return False
        else:
            return in_order(left[1:], right[1:])
    if isinstance(left[0], list) and isinstance(right[0], list):
        if left[0] == right[0]:
            return in_order(left[1:], right[1:])
        else:
            return in_order(left[0], right[0])
    if isinstance(left[0], int) and isinstance(right[0], list):
        if [left[0]] == right[0]:
            return in_order(left[1:], right[1:])
        else:
            return in_order([left[0]], right[0])
    if isinstance(left[0], list) and isinstance(right[0], int):
        if left[0] == [right[0]]:
            return in_order(left[1:], right[1:])
        else:
            return in_order(left[0], [right[0]])
    return in_order(left[1:], right[1:])


def day_13_part2(input_file: str) -> tuple[int, int, int]:
    pairs = parse_inputs(input_file)

    # print(in_order(eval("[7, 7]"), eval("[7]")))

    lt2 = 1
    lt6 = 2
    for item in pairs:
        res = in_order(item, [[2]])
        if res:
            lt2 += 1
        if in_order(item, [[6]]):
            lt6 += 1

    return (lt2, lt6, lt2 * lt6)


if __name__ == "__main__":
    print(day_13_part1(INPUT_FILE))
    print(day_13_part2(INPUT_FILE))
