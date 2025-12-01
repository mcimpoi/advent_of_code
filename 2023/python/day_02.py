# https://adventofcode.com/2023/day/2


INPUT_FILE: str = "2023/data/day_02.txt"
BUDGET_LIMITS: dict[str, int] = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


class Game:
    id: int
    rounds: list[dict[str, int]]

    def __init__(self, id: int, rounds: list[dict[str, int]]):
        self.id = id
        self.rounds = rounds

    def __repr__(self) -> str:
        return f"Game(id={self.id}, rounds={self.rounds})"


def parse_round(round_string: str) -> dict[str, int]:
    round_parts = [x.strip() for x in round_string.split(",")]
    return {color: int(number) for number, color in [x.split(" ") for x in round_parts]}


def get_input(input_file: str) -> list[Game]:
    with open(input_file, "r") as f:
        lines = [x.strip() for x in f.readlines()]

    games = []
    for line in lines:
        game_part = line.split(":")
        game_id = int(game_part[0].split(" ")[1])
        round_strings = [x.strip() for x in game_part[1].split(";")]
        games.append(Game(id=game_id, rounds=[parse_round(x) for x in round_strings]))

    return games


def is_valid(game: Game, budget: int) -> bool:
    for game_round in game.rounds:
        for color, number in game_round.items():
            if number > budget[color]:
                return False
    return True


def get_game_power(game: Game) -> int:
    current_game = {"red": 0, "green": 0, "blue": 0}
    for round in game.rounds:
        for color, number in round.items():
            current_game[color] = max(current_game[color], number)
    result = 1
    for _, number in current_game.items():
        result *= number
    return result


def solve_day_02_part_1(input_file: str = INPUT_FILE):
    result = 0
    games = get_input(input_file)
    for game in games:
        if is_valid(game, BUDGET_LIMITS):
            result += game.id
    return result


def solve_day_02_part_2(input_file: str = INPUT_FILE):
    result = 0
    games = get_input(input_file)
    for game in games:
        result += get_game_power(game)
    return result


if __name__ == "__main__":
    print(f"Solution for Part 1: {solve_day_02_part_1(INPUT_FILE)}")
    print(f"Solution for Part 2: {solve_day_02_part_2(INPUT_FILE)}")
