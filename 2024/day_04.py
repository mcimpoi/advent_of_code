# https://adventofcode.com/2024/day/4
small_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def solve_day_04_p1(grid):
    def in_range(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

    xmas_str = "XMAS"
    res = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "X":
                continue

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    ok = True

                    for k in range(1, 4):
                        if in_range(i + k * dx, j + k * dy):
                            if grid[i + k * dx][j + k * dy] != xmas_str[k]:
                                ok = False
                        else:
                            ok = False
                            break
                    if ok:
                        res += 1

    return res


def solve_day_04_p2(grid):
    def in_range(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

    # NOTE: SAS * MAM will be rotation of SMSM
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "A":
                continue
            if not (
                in_range(i + 1, j + 1)
                and in_range(i - 1, j - 1)
                and in_range(i + 1, j - 1)
                and in_range(i - 1, j + 1)
            ):
                continue

            # MAS * MAS --> clockwise MMSS, ...
            mstr = (
                grid[i - 1][j - 1]
                + grid[i - 1][j + 1]
                + grid[i + 1][j + 1]
                + grid[i + 1][j - 1]
            )

            if mstr in ("MMSS", "SSMM", "MSSM", "SMMS"):
                res += 1

    return res


if __name__ == "__main__":
    grid = [list(row) for row in small_input.split("\n")]
    print(solve_day_04_p1(small_input.split("\n")))  # 18
    print(solve_day_04_p2(grid))  # 9
