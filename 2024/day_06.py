import copy


def parse_grid(input_text):
    grid = []
    for line in input_text.split("\n"):
        grid.append(list(line))
    return grid


def get_start_position(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "^":
                return (y, x)


def solve_part_1(grid):
    def in_bounds(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    start_position = get_start_position(grid)
    x, y = start_position
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    direction_index = 0

    grid[x][y] = "*"
    while in_bounds(x, y):
        dx, dy = directions[direction_index]
        if not in_bounds(x + dx, y + dy):
            break
        if grid[x + dx][y + dy] == "#":
            direction_index = (direction_index + 1) % 4
            dx, dy = directions[direction_index]
        else:
            grid[x + dx][y + dy] = "*"
            x, y = x + dx, y + dy

    return sum(line.count("*") for line in grid)


def print_grid(grid):
    print("\n-----\n")
    for line in grid:
        print("".join(line))
    print("\n=====\n\n")


def solve_part_2(input_grid):
    # print_grid(input_grid)
    # print("\n*****\n\n")

    def in_bounds(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    grid = copy.deepcopy(input_grid)

    start_position = get_start_position(grid)
    x, y = start_position
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    direction_index = 0

    visited = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[x][y] = 0

    grid[x][y] = "*"
    has_cycle = False
    while in_bounds(x, y):
        dx, dy = directions[direction_index]
        if not in_bounds(x + dx, y + dy):
            break
        if grid[x + dx][y + dy] == "#" or grid[x + dx][y + dy] == "O":
            direction_index = (direction_index + 1) % 4
            dx, dy = directions[direction_index]
        else:
            grid[x + dx][y + dy] = "*"
            x, y = x + dx, y + dy
            if visited[x][y] == -1:
                visited[x][y] = direction_index
            else:
                if visited[x][y] == direction_index:
                    has_cycle = True
                    break
    # if has_cycle:
    # print_grid(grid)

    return has_cycle
