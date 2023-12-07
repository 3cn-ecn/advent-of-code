def nb_sol(time, record):
    delta = (time * time - 4 * record) ** (1 / 2)
    x1 = (time - delta) / 2
    x2 = (time + delta) / 2
    return (
        int(x2)
        - int(float.is_integer(x2))
        - int(x1 + 0.999)
        + 1
        + int(float.is_integer(x1))
    )  # can be improved


def part1(input: list[str]):
    times = input[0].split(":")[-1].split()
    distances = input[1].split(":")[-1].split()
    mul_ = 1
    for t, d in zip(times, distances):
        mul_ *= nb_sol(int(t), int(d))
    return mul_


def part2(input: list[str]):
    time = input[0].split(":")[-1].replace(" ", "")
    distance = input[1].split(":")[-1].replace(" ", "")
    return nb_sol(int(time), int(distance))


if __name__ == "__main__":
    with open("input.txt", "r") as f:  # your file here
        input = f.read().splitlines()
        print(part1(input))
        print(part2(input))
