from itertools import groupby


def split_with_indices(s):
    p = 0
    for k, g in groupby(s, lambda x: not str.isnumeric(x)):
        q = p + sum(1 for _ in g)
        if not k:
            yield p, q
        p = q


def is_symbol(char: str) -> bool:
    return not (str.isnumeric(char) or char == ".")


def part1(input: list[str]) -> int:
    sum_ = 0
    for index, line in enumerate(input):
        n = len(line)
        splits = list(split_with_indices(line))
        for start, end in splits:
            number = line[start:end]
            y_pos = []
            if index >= 1:
                y_pos.append(index - 1)
            if index < len(input) - 1:
                y_pos.append(index + 1)
            valid = False

            for x in range(max(start - 1, 0), min(end + 1, n)):
                for y in y_pos:
                    char = input[y][x]
                    if is_symbol(char):
                        valid = True
                        break
                if valid:
                    break

            if is_symbol(line[max(start - 1, 0)]) or is_symbol(
                line[min(end, n - 1)]
            ):
                valid = True

            if valid:
                sum_ += int(number)
    return sum_


def part2(input: list[str]) -> int:
    sum_ = 0
    symbols = [[[] for _ in range(len(input[0]))] for _ in range(len(input))]
    for index, line in enumerate(input):
        n = len(line)
        splits = list(split_with_indices(line))
        for start, end in splits:
            number = int(line[start:end])
            y_pos = []
            if index >= 1:
                y_pos.append(index - 1)
            if index < len(input) - 1:
                y_pos.append(index + 1)

            for x in range(max(start - 1, 0), min(end + 1, n)):
                for y in y_pos:
                    char = input[y][x]
                    if char == "*":
                        symbols[x][y].append(number)

            if line[max(start - 1, 0)] == "*":
                symbols[start - 1][index].append(number)

            if line[min(end, n - 1)] == "*":
                symbols[end][index].append(number)

    for lst in symbols:
        for num_lst in lst:
            if len(num_lst) == 2:
                sum_ += num_lst[0] * num_lst[1]
    return sum_


if __name__ == "__main__":
    with open("input.txt", "r") as f:  # your file here
        input = f.read().splitlines()
        print(part1(input))
        print(part2(input))
