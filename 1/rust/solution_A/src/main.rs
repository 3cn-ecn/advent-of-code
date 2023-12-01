fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let mut sum = 0u32;
    for line_ in std::fs::read_to_string("input.txt").unwrap().lines() {
        let mut digits = vec![];
        for c in line_.chars() {
            if c.is_ascii_digit() {
                digits.push(c.to_digit(10).unwrap());
            }
        }
        sum += digits.first().unwrap() * 10 + digits.last().unwrap();
    }
    sum
}

fn part2() -> u32 {
    let map: std::collections::HashMap<&str, u32> = std::collections::HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]);
    let mut sum = 0u32;
    for line_ in std::fs::read_to_string("input.txt").unwrap().lines() {
        let mut digits = vec![];
        let mut buff = String::new();
        for c in line_.chars() {
            buff.push(c);
            if c.is_ascii_digit() {
                digits.push(c.to_digit(10).unwrap());
                buff.clear();
            } else if buff.chars().count() >= 3 {
                for i in 0..buff.chars().count() - 2 {
                    if let Some(value) = map.get(&buff[i..]) {
                        digits.push(*value)
                    }
                }
            }
        }
        sum += digits.first().unwrap() * 10 + digits.last().unwrap();
    }
    sum
}
