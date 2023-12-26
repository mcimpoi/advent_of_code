// https://adventofcode.com/2023/day/1
use std::fs::File;
use std::io::{self, Read};
use std::path::Path;

const TEXT_DIGITS: [&str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

fn read_file_contents(input_fname: impl AsRef<Path>) -> io::Result<String> {
    let file_path = input_fname.as_ref();
    let mut input = File::open(file_path)?;
    let mut contents = String::new();
    input.read_to_string(&mut contents)?;

    Ok(contents)
}

fn process_line(line: &str, with_text: bool) -> (i32, i32) {
    let mut first_digit = -1;
    let mut last_digit = -1;

    for (i, ch) in line.chars().enumerate() {
        if ch.is_digit(10) {
            last_digit = ch.to_digit(10).unwrap() as i32;
        } else {
            if !with_text {
                continue;
            }
            for (index, text_digit) in TEXT_DIGITS.iter().enumerate() {
                if line[i..].starts_with(text_digit) {
                    last_digit = index as i32 + 1;
                }
            }
        }
        if first_digit == -1 {
            first_digit = last_digit;
        }
    }

    (first_digit, last_digit)
}

pub fn solve_day_01_part_1(input_fname: impl AsRef<Path>) -> i32 {
    let file_contents = read_file_contents(input_fname).expect("Failed to read file");

    let mut result = 0;
    for line in file_contents.lines() {
        let (first_digit, last_digit) = process_line(line, false);
        result += first_digit * 10 + last_digit;
    }
    result
}

pub fn solve_day_01_part_2(input_fname: impl AsRef<Path>) -> i32 {
    let file_contents = read_file_contents(input_fname).expect("Failed to read file");
    let mut result = 0;
    for line in file_contents.lines() {
        let (first_digit, last_digit) = process_line(line, true);
        result += first_digit * 10 + last_digit;
    }

    result
}
