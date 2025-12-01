INPUT_FILE: str = "2022/data/day_08.txt"


def parse_input(input_file: str) -> list[list[int]]:
    with open(input_file, "r") as f:
        data = [x.strip() for x in f.readlines()]

    return [[int(x) for x in line] for line in data]


def day_08_part1(input_file: str) -> int:
    grid = parse_input(input_file)
    visible = [[0 for _ in row] for row in grid]
    for ii in range(len(grid)):
        visible[ii][0] = 1
        visible[ii][-1] = 1
    for ii in range(len(grid[0])):
        visible[0][ii] = 1
        visible[-1][ii] = 1

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            # left:
            ok = True
            for c1 in range(col):
                if grid[row][c1] >= grid[row][col]:
                    ok = False
                    break
            if ok:
                visible[row][col] = 1
                continue
            ok = True
            for c1 in range(col + 1, len(grid[row])):
                if grid[row][c1] >= grid[row][col]:
                    ok = False
                    break
            if ok:
                visible[row][col] = 1
                continue
            ok = True
            for r1 in range(row):
                if grid[r1][col] >= grid[row][col]:
                    ok = False
                    break
            if ok:
                visible[row][col] = 1
                continue
            ok = True
            for r1 in range(row + 1, len(grid)):
                if grid[r1][col] >= grid[row][col]:
                    ok = False
                    break
            if ok:
                visible[row][col] = 1
                continue

    return sum(sum(row) for row in visible)


def day_08_part2(input_file: str) -> int:
    grid = parse_input(input_file)
    maxres = 0

    for rr in range(1, len(grid) - 1):
        for cc in range(1, len(grid[0]) - 1):
            res = 1
            crt = 0
            for c1 in range(cc - 1, -1, -1):
                crt += 1
                if grid[rr][c1] >= grid[rr][cc]:
                    break
            res *= crt

            crt = 0
            for c1 in range(cc + 1, len(grid[rr])):
                crt += 1
                if grid[rr][c1] >= grid[rr][cc]:
                    break
            res *= crt

            crt = 0
            for r1 in range(rr - 1, -1, -1):
                crt += 1
                if grid[r1][cc] >= grid[rr][cc]:
                    break
            res *= crt

            crt = 0
            for r1 in range(rr + 1, len(grid)):
                crt += 1
                if grid[r1][cc] >= grid[rr][cc]:
                    break
            res *= crt
            maxres = max(maxres, res)

    return maxres


if __name__ == "__main__":
    print(day_08_part1(INPUT_FILE))
    print(day_08_part2(INPUT_FILE))
