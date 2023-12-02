fn main() {
    let input = include_str!("../input.txt");
    let result1 = part_1(input);
    println!("{result1}");
    let result2 = part_2(input);
    println!("{result2}");
}

fn part_1(input: &str) -> usize {
    const MAX_RED: i32 = 12;
    const MAX_GREEN: i32 = 13;
    const MAX_BLUE: i32 = 14;

    input.lines().enumerate().fold(0, |acc, (i, line)| {
        let (_, game) = line.split_once(": ").unwrap();
        let subsets = game.split("; ");

        for subset in subsets {
            for pull in subset.split(", ") {
                let (number, colour) = pull.split_once(" ").unwrap();

                let game_not_possible = match colour {
                    "red" => number.parse::<i32>().unwrap() > MAX_RED,
                    "green" => number.parse::<i32>().unwrap() > MAX_GREEN,
                    "blue" => number.parse::<i32>().unwrap() > MAX_BLUE,
                    &_ => true,
                };

                if game_not_possible {
                    return acc;
                }
            }
        }

        return acc + i + 1;
    })
}

fn part_2(input: &str) -> usize {
    input.lines().fold(0, |acc, line| {
        let mut max_red = 0;
        let mut max_green = 0;
        let mut max_blue = 0;

        let (_, game) = line.split_once(": ").unwrap();
        let subsets = game.split("; ");

        for subset in subsets {
            for pull in subset.split(", ") {
                let (number, colour) = pull.split_once(" ").unwrap();

                match colour {
                    "red" => max_red = std::cmp::max(number.parse::<usize>().unwrap(), max_red),
                    "green" => {
                        max_green = std::cmp::max(number.parse::<usize>().unwrap(), max_green)
                    }
                    "blue" => max_blue = std::cmp::max(number.parse::<usize>().unwrap(), max_blue),
                    &_ => (),
                };
            }
        }

        return acc + max_red * max_green * max_blue;
    })
}
