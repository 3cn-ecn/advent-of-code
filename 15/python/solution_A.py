def hash(code: str):
    sum_ = 0
    for c in code:
        sum_ += ord(c)
        sum_ *= 17
        sum_ %= 256
    return sum_


def part1(input: list[str]) -> int:
    codes = input[0].split(",")
    return sum([hash(code) for code in codes])


def part2(input: list[str]) -> int:
    boxes = [[] for _ in range(256)]
    codes = input[0].split(",")
    for code in codes:
        label = code.replace("=", "-").split("-")[0]
        box_index = hash(label)
        if "-" in code:
            try:
                index = [e[0] for e in boxes[box_index]].index(label)
                boxes[box_index].pop(index)
            except ValueError:
                ...
        elif "=" in code:
            lens = code.split("=")[-1]
            try:
                index = [e[0] for e in boxes[box_index]].index(label)
                boxes[box_index][index][1] = lens
            except ValueError:
                boxes[box_index].append([label, lens])
    sum_ = 0
    for j, box in enumerate(boxes):
        sum_ += (j + 1) * sum(
            [(i + 1) * int(lens[1]) for i, lens in enumerate(box)]
        )
    return sum_


if __name__ == "__main__":
    with open("input.txt", "r") as f:  # your file here
        input = f.read().splitlines()
        print(part1(input))
        print(part2(input))
