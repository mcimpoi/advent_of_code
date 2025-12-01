// https://adventofcode.com/2023/day/2

use std::fs::File;
use std::io::Read;
use std::path::Path;

#[derive(Clone)]
struct GameRound {
    red: i32,
    green: i32,
    blue: i32,
}

struct Game {
    id: i32,
    rounds: Vec<GameRound>,
}

const BUDGET_LIMITS: GameRound = GameRound {
    red: 12,
    green: 13,
    blue: 14,
};

fn parse_game_round(game_round: &str) -> GameRound {
    let mut red: i32 = 0;
    let mut green: i32 = 0;
    let mut blue: i32 = 0;
    for round_part in game_round.trim().split(", ").collect::<Vec<&str>>() {
        let round_part_split = round_part.split(" ").collect::<Vec<&str>>();
        match round_part_split[1] {
            "red" => {
                red = match round_part_split[0].parse::<i32>() {
                    Ok(value) => value,
                    Err(_) => panic!("Invalid number {}", round_part_split[0]),
                }
            }
            "green" => {
                green = match round_part_split[0].parse::<i32>() {
                    Ok(value) => value,
                    Err(_) => panic!("Invalid number {}", round_part_split[0]),
                }
            }
            "blue" => {
                blue = match round_part_split[0].parse::<i32>() {
                    Ok(value) => value,
                    Err(_) => panic!("Invalid number {}", round_part_split[0]),
                }
            }
            _ => panic!("Invalid color {}", round_part_split[1]),
        }
    }
    GameRound {
        red: red,
        green: green,
        blue: blue,
    }
}

fn read_file_contents(input_fname: impl AsRef<Path>) -> Vec<Game> {
    let file_path = input_fname.as_ref();
    let mut input = File::open(file_path).expect("Failed to open file");
    let mut contents = String::new();
    let _ = input
        .read_to_string(&mut contents)
        .expect("Failed to read file");

    let mut games: Vec<Game> = vec![];
    for line in contents.lines() {
        let mut game: Game = Game {
            id: 0,
            rounds: vec![],
        };

        let game_rounds_split = line.split(": ").collect::<Vec<&str>>();
        game.id = game_rounds_split[0].split(" ").collect::<Vec<&str>>()[1]
            .parse::<i32>()
            .unwrap();
        for game_round in game_rounds_split[1].split(";") {
            game.rounds.push(parse_game_round(game_round).clone());
        }
        games.push(game);
    }
    games
}

fn is_game_valid(game: &Game, budget_limits: GameRound) -> bool {
    for game_round in &game.rounds {
        if game_round.red > budget_limits.red
            || game_round.green > budget_limits.green
            || game_round.blue > budget_limits.blue
        {
            return false;
        }
    }
    true
}

fn get_game_power(game: &Game) -> i32 {
    let mut game_max: GameRound = GameRound {
        red: 0,
        green: 0,
        blue: 0,
    };

    for game_round in &game.rounds {
        game_max.red = game_max.red.max(game_round.red);
        game_max.green = game_max.green.max(game_round.green);
        game_max.blue = game_max.blue.max(game_round.blue);
    }
    game_max.red * game_max.green * game_max.blue
}

pub fn solve_day_02_part_1(input_fname: impl AsRef<Path>) -> i32 {
    let mut result: i32 = 0;
    let games = read_file_contents(input_fname);
    for game in games {
        if is_game_valid(&game, BUDGET_LIMITS) {
            result += game.id;
        }
    }
    result
}

pub fn solve_day_02_part_2(input_fname: impl AsRef<Path>) -> i32 {
    let mut result: i32 = 0;
    let games = read_file_contents(input_fname);
    for game in games {
        result += get_game_power(&game);
    }
    result
}
