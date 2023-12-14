# https://adventofcode.com/2023/day/13

INPUT_FILE: str = "2023/data/day_13.txt"


def get_puzzles(input_fname):
    with open(input_fname, "r") as input_file:
        input_text = input_file.read()

    lines = input_text.strip().split("\n")

    puzzles = []
    crt_puzzle = []
    for line in lines:
        if line != "":
            crt_puzzle.append(line)
        else:
            puzzles.append(tuple(crt_puzzle))
            crt_puzzle = []
    puzzles.append(tuple(crt_puzzle))
    return puzzles


def get_row_cols(puzzle):
    n_rows = len(puzzle)
    n_cols = len(puzzle[0])

    rows = []
    cols = []

    for row in puzzle:
        bin_row = "".join(["1" if ch == "#" else "0" for ch in row])
        rows.append(bin_row)
    for c in range(n_cols):
        col = ""
        for r in range(n_rows):
            col += "1" if puzzle[r][c] == "#" else "0"
        cols.append(col)

    return tuple(rows), tuple(cols)


def find_horizontal_line(rows):
    result = []
    for candidate in range(1, len(rows)):
        top = candidate - 1
        bottom = candidate

        ok = True

        while top >= 0 and bottom < len(rows):
            ok = rows[top] == rows[bottom]
            if not ok:
                break
            top -= 1
            bottom += 1

        if ok:
            result.append(candidate)
    return result


def find_vertical_line(cols):
    result = []
    for candidate in range(1, len(cols)):
        top = candidate - 1
        bottom = candidate

        ok = True

        while top >= 0 and bottom < len(cols):
            ok = cols[top] == cols[bottom]
            if not ok:
                break
            top -= 1
            bottom += 1

        if ok:
            result.append(candidate)
    return result


def patch_puzzle(p_rows, p_cols, r, c):
    puzzle_rows = list(p_rows)
    puzzle_cols = list(p_cols)

    old_row = [int(x) for x in list(puzzle_rows[r])]
    old_row[c] = 1 - old_row[c]
    old_row = "".join(str(x) for x in old_row)
    puzzle_rows[r] = old_row

    old_col = [int(x) for x in list(puzzle_cols[c])]
    old_col[r] = 1 - old_col[r]
    old_col = "".join(str(x) for x in old_col)
    puzzle_cols[c] = old_col

    return tuple(puzzle_rows), tuple(puzzle_cols)


def solve_day_13_part_01(input_fname: str) -> int:
    puzzles = get_puzzles(input_fname)
    horiz, vert = 0, 0
    for puzzle in puzzles:
        rows, cols = get_row_cols(puzzle)
        hl = find_horizontal_line(rows)
        vl = find_vertical_line(cols)
        if len(hl) == 1:
            horiz += hl[0]
        elif len(vl) == 1:
            vert += vl[0]
    return horiz * 100 + vert


def solve_day_13_part_02(input_fname: str) -> int:
    puzzles = get_puzzles(input_fname)

    horiz_total = 0
    vert_total = 0
    for ip, puzzle in enumerate(puzzles):
        rows, cols = get_row_cols(puzzle)
        hl = find_horizontal_line(rows)
        vl = find_vertical_line(cols)

        patched_hl = []
        patched_vl = []
        for rr in range(len(rows)):
            for cc in range(len(cols)):
                patched_rows, patched_cols = patch_puzzle(rows, cols, rr, cc)
                patched_hl += find_horizontal_line(patched_rows)
                patched_vl += find_vertical_line(patched_cols)

                patched_hl = list(set(patched_hl))
                patched_vl = list(set(patched_vl))

        if len(patched_hl) == 2:
            horiz_total += sum(patched_hl) - hl[0]
        elif len(patched_vl) == 2:
            vert_total += sum(patched_vl) - vl[0]
        elif len(hl) == 0 and len(patched_hl) == 1:
            horiz_total += patched_hl[0]
        elif len(vl) == 0 and len(patched_vl) == 1:
            vert_total += patched_vl[0]
        else:
            print("This should not happen: ", ip, hl, patched_hl, vl, patched_vl)

    return horiz_total * 100 + vert_total


if __name__ == "__main__":
    print(solve_day_13_part_01(INPUT_FILE))
    print(solve_day_13_part_02(INPUT_FILE))
