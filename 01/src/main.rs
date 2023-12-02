use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    part_1();
    part_2();
}

fn part_1() {
    let mut sum = 0;
    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(line) = line {
                let digits: Vec<char> = line.chars().filter(|c| c.is_digit(10)).collect();

                if let Some(fst) = digits.first() {
                    if let Some(lst) = digits.last() {
                        sum += format!("{fst}{lst}").parse::<i32>().unwrap();
                    } else {
                        sum += format!("{fst}{fst}").parse::<i32>().unwrap();
                    }
                }
            }
        }
    }

    println!("{sum}");
}

fn part_2() {
    let mut sum = 0;
    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(line) = line {
                let mut acc = Vec::new();
                let chars = line.chars();

                for (i, char) in chars.clone().enumerate() {
                    if char.is_digit(10) {
                        acc.push(char.to_digit(10).unwrap())
                    } else {
                        match chars
                            .clone()
                            .skip(i)
                            .take(3)
                            .into_iter()
                            .collect::<String>()
                            .as_str()
                        {
                            "one" => acc.push(1),
                            "two" => acc.push(2),
                            "six" => acc.push(6),
                            _ => (),
                        };
                        match chars
                            .clone()
                            .skip(i)
                            .take(4)
                            .into_iter()
                            .collect::<String>()
                            .as_str()
                        {
                            "four" => acc.push(4),
                            "five" => acc.push(5),
                            "nine" => acc.push(9),
                            _ => (),
                        }
                        match chars
                            .clone()
                            .skip(i)
                            .take(5)
                            .into_iter()
                            .collect::<String>()
                            .as_str()
                        {
                            "three" => acc.push(3),
                            "seven" => acc.push(7),
                            "eight" => acc.push(8),
                            _ => (),
                        }
                    }
                }

                if let Some(fst) = acc.first() {
                    if let Some(lst) = acc.last() {
                        sum += format!("{fst}{lst}").parse::<i32>().unwrap();
                    } else {
                        sum += format!("{fst}{fst}").parse::<i32>().unwrap();
                    }
                }
            }
        }
    }

    println!("{sum}");
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
