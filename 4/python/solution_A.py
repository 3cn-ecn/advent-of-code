def part1(input: list[str]) -> int:
    sum_ = 0
    for card in input:
        winning, numbers = card.split(":")[-1].split("|")
        winning_lst = winning.split()
        numbers_lst = numbers.split()
        winning_count = len(set(winning_lst).intersection(numbers_lst))
        sum_ += 2 ** (winning_count - 1) if winning_count > 0 else 0
    return sum_


def part2(input: list[str]) -> int:
    counts_ = [1 for _ in range(len(input))]
    for index, card in enumerate(input):
        winning, numbers = card.split(":")[-1].split("|")
        winning_lst = winning.split()
        numbers_lst = numbers.split()
        winning_count = len(set(winning_lst).intersection(numbers_lst))
        for i in range(winning_count):
            counts_[index + i + 1] += counts_[index]
    return sum(counts_)


if __name__ == "__main__":
    with open("input.txt", "r") as f:  # your file here
        input = f.read().splitlines()
        print(part1(input))
        print(part2(input))
