// Runner for Advent of Code.
// import module day_XX and
// call solve_day_XX_part_1 and solve_day_XX_part_2

// Assumes inputs are in data/day_XX.txt
mod day_03;

use day_03::{solve_day_03_part_1, solve_day_03_part_2};

fn main() {
    println!(
        "Result (small): {}",
        solve_day_03_part_1("data/day_03_small.txt")
    );
    println!(
        "Result (small): {}",
        solve_day_03_part_2("data/day_03_small.txt")
    );
    println!("Result: {}", solve_day_03_part_1("data/day_03.txt"));
    println!("Result: {}", solve_day_03_part_2("data/day_03.txt"));
}
