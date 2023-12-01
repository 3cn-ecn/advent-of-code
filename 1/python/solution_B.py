import re

# Solutions using regex


def part1(input: list[str]):
    sum_ = 0
    pattern = re.compile(r"(\d).*(\d)|(?=(\d))(\d)")
    for e in input:
        match = pattern.search(e)
        sum_ += int(match.expand(r"\1\2\3\4"))
    return sum_


def part2(input: list[str]):
    name_to_digit = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    sum_ = 0
    digit_class = "|".join(name_to_digit.keys()) + r"|\d"
    pattern = re.compile(
        rf"({digit_class}).*({digit_class})|(?=({digit_class}))({digit_class})"
    )
    for e in input:
        match = pattern.search(e)
        groups = list(filter(None, match.groups()))
        for i in range(2):
            groups[i] = name_to_digit.get(groups[i]) or groups[i]
        sum_ += int("".join(groups))
    return sum_


if __name__ == "__main__":
    with open("input.txt") as f:  # your file here
        input = f.readlines()
        print(part1(input))
        print(part2(input))
