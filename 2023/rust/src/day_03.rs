// https://adventofcode.com/2023/day/3

use std::fs::File;
use std::io::Read;
use std::path::Path;

struct Number {
    value: i32,
    start: i32,
    end: i32,
    row: i32,
}

struct Symbol {
    value: char,
    row: i32,
    col: i32,
}

fn read_file_contents(input_fname: impl AsRef<Path>) -> (Vec<Number>, Vec<Symbol>) {
    let file_path = input_fname.as_ref();
    let mut input = File::open(file_path).expect("Failed to open file");
    let mut contents = String::new();
    let _ = input
        .read_to_string(&mut contents)
        .expect("Failed to read file");

    let mut numbers: Vec<Number> = Vec::new();
    let mut symbols: Vec<Symbol> = Vec::new();

    let mut row = 0;

    for line in contents.lines() {
        row += 1;
        let mut col = 0;
        let extended_line = format!("{}{}", line, ".");
        let mut crt_number = String::new();
        let mut num_start = -1;
        let mut num_end = -1;
        for c in extended_line.chars() {
            col += 1;

            if c.is_digit(10) {
                crt_number.push(c);
                num_end = col;
                if num_start == -1 {
                    num_start = col;
                }
            } else {
                if crt_number.len() > 0 {
                    numbers.push(Number {
                        value: match crt_number.parse::<i32>() {
                            Ok(value) => value,
                            Err(_) => panic!("Invalid number {}", crt_number),
                        },
                        start: num_start,
                        end: num_end,
                        row: row,
                    });
                }

                if c != '.' {
                    symbols.push(Symbol {
                        value: c,
                        row: row,
                        col: col,
                    });
                }

                crt_number = String::new();
                num_start = -1;
                num_end = -1;
            }
        }
    }

    (numbers, symbols)
}

fn is_adjacent(number: &Number, symbol: &Symbol) -> bool {
    (number.row - symbol.row).abs() <= 1
        && number.start - 1 <= symbol.col
        && symbol.col <= number.end + 1
}

pub fn solve_day_03_part_1(input_fname: impl AsRef<Path>) -> i32 {
    let (numbers, symbols) = read_file_contents(input_fname);
    let mut result = 0;

    for number in &numbers {
        for symbol in &symbols {
            if is_adjacent(number, symbol) {
                result += number.value;
            }
        }
    }

    result
}

pub fn solve_day_03_part_2(input_fname: impl AsRef<Path>) -> i32 {
    let (numbers, symbols) = read_file_contents(input_fname);
    let mut result = 0;

    for symbol in &symbols {
        if symbol.value != '*' {
            continue;
        }
        let mut first = -1;
        let mut second = -1;
        let mut more_than_two = false;
        for number in &numbers {
            if is_adjacent(number, symbol) {
                if first == -1 {
                    first = number.value;
                } else {
                    if second == -1 {
                        second = number.value;
                    } else {
                        more_than_two = true;
                    }
                }
            }
        }
        if more_than_two {
            continue;
        }
        if first != -1 && second != -1 {
            result += first * second;
        }
    }

    result
}
