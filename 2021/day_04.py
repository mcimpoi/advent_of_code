from collections import defaultdict

INPUT_FILE = "data/day_04.txt"

ZERO_VAL = 10000
BOARD_SZ = 5


def solve_day4_p1(input_file: str) -> int:
    with open(input_file, "r") as f:
        lines = [line_.strip() for line_ in f.readlines() if len(line_) > 1]

    first_line = [int(x) if x != "0" else 10000 for x in lines[0].split(",")]

    max_val = max(first_line)

    lines = lines[1:]
    boards = []

    for ii in range(len(lines) // BOARD_SZ):
        board = " ".join(lines[BOARD_SZ * ii + x] for x in range(BOARD_SZ))
        board = [int(x) if x != "0" else 10000 for x in board.split()]
        boards.append(board)

        max_val = max(max_val, max(board))

    print(len(board))
    print(max_val)

    for num in first_line:
        for board in boards:
            found = False
            for rr in range(BOARD_SZ):
                for cc in range(BOARD_SZ):
                    if board[rr * BOARD_SZ + cc] == num:
                        board[rr * BOARD_SZ + cc] *= -1
                        found = True
                        if check_board(board, rr, cc):
                            print_board(board)
                            return board_val(board, num)
                        break

    return 0


def solve_day4_p2(input_file: str) -> int:
    with open(input_file, "r") as f:
        lines = [line_.strip() for line_ in f.readlines() if len(line_) > 1]

    first_line = [int(x) if x != "0" else 10000 for x in lines[0].split(",")]

    max_val = max(first_line)

    lines = lines[1:]
    boards = []

    for ii in range(len(lines) // BOARD_SZ):
        board = " ".join(lines[BOARD_SZ * ii + x] for x in range(BOARD_SZ))
        board = [int(x) if x != "0" else 10000 for x in board.split()]
        boards.append(board)

        max_val = max(max_val, max(board))

    print(len(board))
    print(max_val)

    winner = [0] * len(boards)

    for num in first_line:
        for bb, board in enumerate(boards):
            if winner[bb]:
                continue
            found = False
            for rr in range(BOARD_SZ):
                for cc in range(BOARD_SZ):
                    if board[rr * BOARD_SZ + cc] == num:
                        board[rr * BOARD_SZ + cc] *= -1
                        found = True
                        if check_board(board, rr, cc):
                            winner[bb] = 1
                            last_winner, last_num = bb, num

    print_board(boards[last_winner])
    return board_val(boards[last_winner], last_num)


def print_board(board):
    for rr in range(BOARD_SZ):
        line = ""
        for cc in range(BOARD_SZ):
            line += f"{board[rr * BOARD_SZ + cc]: 16d}"
        print(line)


def check_board(board, rr, cc) -> bool:
    cnt1, cnt2 = 0, 0
    for r1 in range(BOARD_SZ):
        if (board[BOARD_SZ * r1 + cc] < 0):
            cnt1 += 1

    for c1 in range(BOARD_SZ):
        if (board[BOARD_SZ * rr + c1] < 0):
            cnt2 += 1

    return cnt1 == BOARD_SZ or cnt2 == BOARD_SZ


def board_val(board, num) -> int:
    return sum([x for x in board if x > 0]) * num


if __name__ == "__main__":
    print(solve_day4_p1(INPUT_FILE))
    print(solve_day4_p2(INPUT_FILE))
