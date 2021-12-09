from collections import defaultdict
from io import DEFAULT_BUFFER_SIZE
from typing import List, Tuple

INPUT_FILE = "data/day_09.txt"
INPUT_FILE_SMALL = "data/day_09_small.txt"


def parse_input(input_file: str) -> Tuple[List[List[int]], int, int]:
    with open(input_file, "r") as f:
        data = f.readlines()

    matrix = []
    for line in data:
        matrix.append([int(x) for x in line.strip()])

    numRows: int = len(matrix)
    numCols: int = len(matrix[0])

    return matrix, numRows, numCols


def solve_day9_p1(input_file: str) -> int:
    result = 0
    matrix, numRows, numCols = parse_input(input_file)

    for rr in range(numRows):
        for cc in range(numCols):
            min_point = 10
            if rr - 1 >= 0:
                min_point = min(min_point, matrix[rr - 1][cc])
            if cc - 1 >= 0:
                min_point = min(min_point, matrix[rr][cc - 1])
            if rr + 1 < numRows:
                min_point = min(min_point, matrix[rr + 1][cc])
            if cc + 1 < numCols:
                min_point = min(min_point, matrix[rr][cc + 1])
            if min_point > matrix[rr][cc]:
                result += matrix[rr][cc] + 1
                # print(rr, cc, " ", matrix[rr][cc])
    return result


def solve_day9_p2(input_file: str) -> int:
    matrix, numRows, numCols = parse_input(input_file)
    visited = [[0 for _ in range(numCols)] for _ in range(numRows)]

    sizes = []

    for rr in range(numRows):
        for cc in range(numCols):
            if visited[rr][cc] or matrix[rr][cc] == 9:
                continue

            st: List[Tuple[int, int]] = []
            visited[rr][cc] = 1
            sz = 0
            st.append((rr, cc))
            while len(st) > 0:
                crt_r, crt_c = st.pop()
                sz += 1
                if (
                    crt_r - 1 >= 0
                    and visited[crt_r - 1][crt_c] == 0
                    and matrix[crt_r - 1][crt_c] != 9
                ):
                    st.append((crt_r - 1, crt_c))
                    visited[crt_r - 1][crt_c] = 1

                if (
                    crt_r + 1 < numRows
                    and visited[crt_r + 1][crt_c] == 0
                    and matrix[crt_r + 1][crt_c] != 9
                ):
                    st.append((crt_r + 1, crt_c))
                    visited[crt_r + 1][crt_c] = 1

                if (
                    crt_c - 1 >= 0
                    and visited[crt_r][crt_c - 1] == 0
                    and matrix[crt_r][crt_c - 1] != 9
                ):
                    st.append((crt_r, crt_c - 1))
                    visited[crt_r][crt_c - 1] = 1

                if (
                    crt_c + 1 < numCols
                    and visited[crt_r][crt_c + 1] == 0
                    and matrix[crt_r][crt_c + 1] != 9
                ):
                    st.append((crt_r, crt_c + 1))
                    visited[crt_r][crt_c + 1] = 1

            sizes.append(sz)

    print(sizes)
    sizes.sort(reverse=True)

    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    print(solve_day9_p1(INPUT_FILE_SMALL))
    print(solve_day9_p1(INPUT_FILE))
    print(solve_day9_p2(INPUT_FILE_SMALL))
    print(solve_day9_p2(INPUT_FILE))
