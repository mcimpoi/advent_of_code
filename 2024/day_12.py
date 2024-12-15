def read_input(input_fname):
    with open(input_fname, "r") as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]


def zeros_like(grid):
    return [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]


def padded_zeros_like(grid):
    return [[0 for _ in range(len(grid[0]) + 2)] for _ in range(len(grid) + 2)]


def solve(grid):
    res = 0
    visited = zeros_like(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j]:
                continue
            perimeter = 0
            area = 0
            stack = [(i, j)]
            visited[i][j] = 1
            while stack:
                x, y = stack.pop()
                area += 1
                temp_p = 4
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                        continue
                    if grid[nx][ny] == grid[x][y]:
                        temp_p -= 1
                perimeter += temp_p

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < len(grid)
                        and 0 <= ny < len(grid[0])
                        and not visited[nx][ny]
                        and grid[nx][ny] == grid[x][y]
                    ):

                        stack.append((nx, ny))
                        visited[nx][ny] = 1
            res += area * perimeter
    return res


def print_grid(grid):
    for row in grid:
        print("".join(map(str, row)))
    print()


def count_corners(mask):
    res = 0
    for i in range(1, len(mask) - 1):
        for j in range(1, len(mask[0]) - 1):
            if mask[i][j] == 0:
                continue
            if mask[i - 1][j] == 0 and mask[i][j - 1] == 0:
                res += 1
            if mask[i - 1][j] == 0 and mask[i][j + 1] == 0:
                res += 1

            if mask[i + 1][j] == 0 and mask[i][j - 1] == 0:
                res += 1
            if mask[i + 1][j] == 0 and mask[i][j + 1] == 0:
                res += 1

            if mask[i][j - 1] == 1 and mask[i + 1][j] == 1 and mask[i + 1][j - 1] == 0:
                res += 1
            if mask[i][j - 1] == 1 and mask[i - 1][j] == 1 and mask[i - 1][j - 1] == 0:
                res += 1
            if mask[i][j + 1] == 1 and mask[i + 1][j] == 1 and mask[i + 1][j + 1] == 0:
                res += 1
            if mask[i][j + 1] == 1 and mask[i - 1][j] == 1 and mask[i - 1][j + 1] == 0:
                res += 1
    return res


def solve_part_2(grid):
    res = 0
    visited = zeros_like(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j]:
                continue
            mask = padded_zeros_like(grid)
            area = 0
            stack = [(i, j)]
            visited[i][j] = 1
            mask[i + 1][j + 1] = 1
            while stack:
                x, y = stack.pop()
                area += 1

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < len(grid)
                        and 0 <= ny < len(grid[0])
                        and not visited[nx][ny]
                        and grid[nx][ny] == grid[x][y]
                    ):

                        stack.append((nx, ny))
                        visited[nx][ny] = 1
                        mask[nx + 1][ny + 1] = 1
            n_corners = count_corners(mask)
            # print(grid[i][j], n_corners)
            res += area * n_corners
    return res


if __name__ == "__main__":
    grid = read_input("2024/day_12_large.txt")
    print(solve_part_2(grid))
