tiny_input_day_04: str = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def parse_grid(grid_str: str) -> list[str]:
    return [list(x.strip()) for x in grid_str.splitlines()]


def to_remove_rolls(grid: list[list[str]]) -> list[tuple[int, int]]:
    n_rows, n_cols = len(grid), len(grid[0])
    res = []
    for row in range(n_rows):
        for col in range(n_cols):
            if grid[row][col] == "@":
                neighbors = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr == 0 and dc == 0:
                            continue
                        if (
                            0 <= row + dr < n_rows
                            and 0 <= col + dc < n_cols
                            and grid[row + dr][col + dc] == "@"
                        ):
                            neighbors += 1
                if neighbors < 4:
                    res.append((row, col))
    return res


def solve_day_04_part_1(grid_str: str) -> int:
    return len(to_remove_rolls(parse_grid(grid_str)))


def solve_day_04_part_2(grid_str: str) -> int:
    grid = parse_grid(grid_str)
    total_remove = 0
    to_remove = to_remove_rolls(grid)
    while to_remove:
        total_remove += len(to_remove)
        for row, col in to_remove:
            grid[row][col] = "."
        to_remove = to_remove_rolls(grid)

    return total_remove


if __name__ == "__main__":
    part1_solution = solve_day_04_part_1(tiny_input_day_04)
    print(f"Part 1 Solution: {part1_solution} | Expected: 13")

    part2_solution = solve_day_04_part_2(tiny_input_day_04)
    print(f"Part 2 Solution: {part2_solution} | Expected: 43")
