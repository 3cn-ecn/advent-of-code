def part1(input: list[str]) -> int:
    sum_ = 0
    for line in input:
        sequence = [[int(e) for e in line.split()]]
        while any(sequence[-1]) and len(sequence[-1]) > 1:
            buff = []
            for i in range(len(sequence[-1]) - 1):
                buff.append(sequence[-1][i + 1] - sequence[-1][i])
            sequence.append(buff)
        sequence[-1].append(0)
        for i in range(len(sequence) - 2, -1, -1):
            sequence[i].append(sequence[i][-1] + sequence[i + 1][-1])
        sum_ += sequence[0][-1]
    return sum_


def part2(input: list[str]) -> int:
    sum_ = 0
    for line in input:
        sequence = [[int(e) for e in line.split()]]
        while any(sequence[-1]) and len(sequence[-1]) > 1:
            buff = []
            for i in range(len(sequence[-1]) - 1):
                buff.append(sequence[-1][i + 1] - sequence[-1][i])
            sequence.append(buff)
        sequence[-1].insert(0, 0)
        for i in range(len(sequence) - 2, -1, -1):
            sequence[i].insert(0, sequence[i][0] - sequence[i + 1][0])
        sum_ += sequence[0][0]
    return sum_


if __name__ == "__main__":
    with open("input.txt", "r") as f:  # your file here
        input = f.read().splitlines()
        print(part1(input))
        print(part2(input))
