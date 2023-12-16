# https://adventofcode.com/2023/day/15

INPUT_FILE = "2023/data/day_15.txt"


def get_input_line(input_file: str) -> str:
    with open(input_file) as f:
        return f.read().strip()


def hash_one(token: str) -> int:
    crt = 0
    for ch in token:
        crt += ord(ch)
        crt = crt * 17
        crt = crt % 256
    return crt


def solve_day_15_part_01(input_line: str) -> int:
    return sum([hash_one(x) for x in input_line.split(",")])


def solve_day_15_part_02(input_line: str) -> int:
    n_boxes = 256
    boxes = [[] for _ in range(n_boxes)]

    for step in input_line.split(","):
        label, focal_length = step.replace("=", "-").split("-")
        dest_box = hash_one(label)
        if focal_length == "":
            for idx, lens in enumerate(boxes[dest_box]):
                if lens[0] == label:
                    boxes[dest_box].pop(idx)
                    break
        else:
            for idx, lens in enumerate(boxes[dest_box]):
                if lens[0] == label:
                    boxes[dest_box][idx] = (label, int(focal_length))
                    break
            else:
                boxes[dest_box].append((label, int(focal_length)))

    total = 0
    for idx_box, box in enumerate(boxes):
        for idx_lens, lens in enumerate(box):
            total += (idx_box + 1) * (idx_lens + 1) * lens[1]

    return total


if __name__ == "__main__":
    INPUT_LINE = get_input_line(INPUT_FILE)
    print(f"Part 1: {solve_day_15_part_01(INPUT_LINE)}")
    print(f"Part 2: {solve_day_15_part_02(INPUT_LINE)}")
