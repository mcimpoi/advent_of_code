from collections import defaultdict


def read_grid(filename):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f]


def solve_day_08(filename):
    grid = read_grid(filename)

    coords = defaultdict(list)

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == ".":
                continue
            coords[col].append([r, c])

    # print(coords)
    result = []
    for _, v in coords.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                dr, dc = v[j][0] - v[i][0], v[j][1] - v[i][1]
                ar1, ac1 = v[i][0] - dr, v[i][1] - dc
                ar2, ac2 = v[j][0] + dr, v[j][1] + dc
                if 0 <= ar1 < len(grid) and 0 <= ac1 < len(grid[0]):
                    result.append((ar1, ac1))
                    grid[ar1][ac1] = "#"
                if 0 <= ar2 < len(grid) and 0 <= ac2 < len(grid[0]):
                    result.append((ar2, ac2))
                    grid[ar2][ac2] = "#"

    for r, row in enumerate(grid):
        print("".join(row))
    return len(set(result))


def solve_day_08_part2(filename):
    grid = read_grid(filename)

    coords = defaultdict(list)

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == ".":
                continue
            coords[col].append([r, c])

    # print(coords)
    result = []
    for _, v in coords.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                dr, dc = v[j][0] - v[i][0], v[j][1] - v[i][1]
                for k in range(-100, 100):
                    ar1, ac1 = v[i][0] - k * dr, v[i][1] - k * dc

                    if 0 <= ar1 < len(grid) and 0 <= ac1 < len(grid[0]):
                        result.append((ar1, ac1))

    return len(set(result))


if __name__ == "__main__":
    print(solve_day_08_part2("2024/z_day_08L.txt"))
