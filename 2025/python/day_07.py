from collections import defaultdict


def solve_day_7_p1(input_str):
    lines = [x.strip() for x in input_str.strip().splitlines()]
    print(lines[0])

    idx_s = [i for i, ch in enumerate(lines[0]) if ch == "S"][0]

    n_rows = len(lines)
    n_cols = len(lines[0])
    print(n_rows, n_cols)
    visited = defaultdict(lambda: defaultdict(lambda: False))
    st = []
    st.append((0, idx_s))
    res = set()
    while st:
        crt_r, crt_c = st.pop()
        # print(crt_c, crt_r)
        if crt_r == n_rows - 1:
            continue
        if lines[crt_r + 1][crt_c] == ".":
            st.append((crt_r + 1, crt_c))
        elif lines[crt_r + 1][crt_c] == "^":
            res.add((crt_r + 1, crt_c))
            if not visited[crt_r + 1][crt_c - 1]:
                st.append((crt_r + 1, crt_c - 1))
                visited[crt_r + 1][crt_c - 1] = True

            if not visited[crt_r + 1][crt_c + 1]:
                st.append((crt_r + 1, crt_c + 1))
                visited[crt_r + 1][crt_c + 1] = True
    print(len(res))


def solve_day_7_p2(input_str):
    lines = [x.strip() for x in input_str.strip().splitlines()]

    idx_s = [i for i, ch in enumerate(lines[0]) if ch == "S"][0]

    n_rows = len(lines)
    n_cols = len(lines[0])

    # Memoization: cache[row][col] = number of paths from (row, col) to bottom
    cache = {}

    def count_paths(row, col):
        # Base case: reached the bottom row
        if row == n_rows - 1:
            return 1

        # Check cache
        if (row, col) in cache:
            return cache[(row, col)]

        # Out of bounds
        if row + 1 >= n_rows:
            return 0

        next_cell = lines[row + 1][col]
        total_paths = 0

        # Move straight down on empty cell
        if next_cell == ".":
            total_paths = count_paths(row + 1, col)

        # Branch left and right on obstacle
        elif next_cell == "^":
            # Move diagonally down-left
            if col - 1 >= 0:
                total_paths += count_paths(row + 1, col - 1)

            # Move diagonally down-right
            if col + 1 < n_cols:
                total_paths += count_paths(row + 1, col + 1)

        cache[(row, col)] = total_paths
        return total_paths

    result = count_paths(0, idx_s)
    print(f"Total unique paths: {result}")
    return result


if __name__ == "__main__":
    with open("/tmp/day_07_input.txt", "r") as f:
        input_str = f.read()
    solve_day_7_p2(input_str)
