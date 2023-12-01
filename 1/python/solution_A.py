def part1():
    sum_ = 0
    for line in open("input.txt", "r").readlines():
        digits = []
        for c in filter(lambda c: c.isnumeric(), line):
            digits.append(int(c))
        sum_ += digits[0] * 10 + digits[-1]
    return sum_


def part2():
    map_ = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    sum_ = 0
    for line in open("input.txt", "r").readlines():
        digits = []
        buff = ""
        for c in line:
            buff += c
            if c.isnumeric():
                digits.append(int(c))
                buff = ""
            elif len(buff) >= 3:
                for i in range(len(buff) - 2):
                    if buff[i:] in map_:
                        digits.append(map_[buff[i:]])
        sum_ += digits[0] * 10 + digits[-1]
    return sum_


if __name__ == "__main__":
    print(part1())
    print(part2())
