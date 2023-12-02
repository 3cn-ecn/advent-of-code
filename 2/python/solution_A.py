def part1(input: list[str]):
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    sum_ = 0
    for id, games in enumerate(input, 1):
        game_list = games.split(":")[-1].split(";")
        valid_ = True
        for game in game_list:
            game_set = game.split(",")
            for pick in game_set:
                _, num, col = pick.split(" ")
                if int(num) > max_cubes[col]:
                    valid_ = False
                if not valid_:
                    break
            if not valid_:
                break
        if valid_:
            sum_ += id

    return sum_


def part2(input: list[str]):
    sum_ = 0
    for games in input:
        game_list = games.split(":")[-1].split(";")
        fewest = {"green": 0, "red": 0, "blue": 0}
        for game in game_list:
            game_set = game.split(",")
            for pick in game_set:
                _, num, col = pick.split(" ")
                fewest[col] = max(fewest[col], int(num))

        sum_ += fewest["blue"] * fewest["green"] * fewest["red"]
    return sum_


if __name__ == "__main__":
    with open("input.txt") as f:  # your file here
        input = f.read().splitlines()
        print(part1(input))
        print(part2(input))
