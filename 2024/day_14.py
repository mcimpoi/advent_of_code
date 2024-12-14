def get_input_grid(fname):
    positions, velocities = [], []
    with open(fname, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            parts = line.split(" ")
            position = [int(x) for x in parts[0].split("=")[1].split(",")]
            velocity = [int(x) for x in parts[1].split("=")[1].split(",")]
            positions.append([position[1], position[0]])
            velocities.append([velocity[1], velocity[0]])
    return positions, velocities


def get_quadrants(grid, grid_size):
    quad_1, quad_2, quad_3, quad_4 = 0, 0, 0, 0
    for i in range(grid_size[0] // 2):
        for j in range(grid_size[1] // 2):
            quad_1 += grid[i][j]
        for j in range(grid_size[1] // 2 + 1, grid_size[1]):
            quad_2 += grid[i][j]
    for i in range(grid_size[0] // 2 + 1, grid_size[0]):
        for j in range(grid_size[1] // 2):
            quad_3 += grid[i][j]
        for j in range(grid_size[1] // 2 + 1, grid_size[1]):
            quad_4 += grid[i][j]

    return quad_1, quad_2, quad_3, quad_4


def solve_day_14_part_1(fname, grid_size):
    positions, velocities = get_input_grid(fname)

    n_steps = 100
    for idx, (position, velocity) in enumerate(zip(positions, velocities)):
        new_pos_x = (position[0] + n_steps * velocity[0]) % grid_size[0]
        new_pos_y = (position[1] + n_steps * velocity[1]) % grid_size[1]
        positions[idx] = [new_pos_x, new_pos_y]

    grid = [[0 for _ in range(grid_size[1])] for _ in range(grid_size[0])]
    for position in positions:
        grid[position[0]][position[1]] += 1

    quad_1, quad_2, quad_3, quad_4 = get_quadrants(grid, grid_size)
    return quad_1, quad_2, quad_3, quad_4


import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os
import tqdm


def solve_day_14_part_2(fname, grid_size):
    positions, velocities = get_input_grid(fname)
    os.makedirs("2024/day_14/L", exist_ok=True)
    new_positions = [[0, 0] for _ in range(len(positions))]
    for n_steps in tqdm.tqdm(range(1, 15000)):
        for idx, (position, velocity) in enumerate(zip(positions, velocities)):
            new_pos_x = (position[0] + n_steps * velocity[0]) % grid_size[0]
            new_pos_y = (position[1] + n_steps * velocity[1]) % grid_size[1]
            new_positions[idx] = [new_pos_x, new_pos_y]

        skip = False
        grid = [[0 for _ in range(grid_size[1])] for _ in range(grid_size[0])]
        for position in new_positions:
            grid[position[0]][position[1]] += 1
            if grid[position[0]][position[1]] > 1:
                skip = True

        if skip:
            continue
        print(n_steps)
        fig = plt.figure(frameon=False)
        fig.set_size_inches(3, 3)
        ax = plt.Axes(fig, [0.0, 0.0, 1.0, 1.0])
        ax.set_axis_off()
        fig.add_axes(ax)
        ax.imshow(np.array(grid), cmap="gray")

        fig.savefig(f"2024/day_14/L/fig_{n_steps:08d}.png")
        return n_steps


GRID_SMALL = (7, 11)
GRID_BIG = (103, 101)

if __name__ == "__main__":
    print(solve_day_14_part_1("2024/day_14_small.txt", GRID_SMALL))
    print(solve_day_14_part_1("2024/day_14_large.txt", GRID_BIG))
    print(solve_day_14_part_2("2024/day_14_large.txt", GRID_BIG))
