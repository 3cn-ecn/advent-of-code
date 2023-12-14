def part1(input: list[str]) -> int:
    grid = [[*line] for line in input]
    sum_ = 0
    n = len(grid)
    for y in range(n):
        for x in range(len(grid[0])):
            if grid[y][x] != "O":
                continue
            new_y = y
            while new_y > 0 and grid[new_y - 1][x] == ".":
                new_y -= 1
            grid[y][x] = "."
            grid[new_y][x] = "O"
            sum_ += n - new_y

    return sum_


def north(grid: list[str]):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != "O":
                continue
            new_y = y
            while new_y > 0 and grid[new_y - 1][x] == ".":
                new_y -= 1
            grid[y][x] = "."
            grid[new_y][x] = "O"


def south(grid: list[str]):
    for y in range(len(grid) - 1, -1, -1):
        for x in range(len(grid[0])):
            if grid[y][x] != "O":
                continue
            new_y = y
            while new_y < len(grid) - 1 and grid[new_y + 1][x] == ".":
                new_y += 1
            grid[y][x] = "."
            grid[new_y][x] = "O"


def west(grid: list[str]):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] != "O":
                continue
            new_x = x
            while new_x > 0 and grid[y][new_x - 1] == ".":
                new_x -= 1
            grid[y][x] = "."
            grid[y][new_x] = "O"


def east(grid: list[str]):
    for x in range(len(grid[0]) - 1, -1, -1):
        for y in range(len(grid)):
            if grid[y][x] != "O":
                continue
            new_x = x
            while new_x < len(grid[0]) - 1 and grid[y][new_x + 1] == ".":
                new_x += 1
            grid[y][x] = "."
            grid[y][new_x] = "O"


def score(grid):
    sum_ = 0
    n = len(grid)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == "O":
                sum_ += n - y
    return sum_


def part2(input: list[str]) -> int:
    grid = [[*line] for line in input]
    prev_grids: list[str] = []
    scores = []
    stringified = "".join(["".join(line) for line in grid])
    while True:
        prev_grids.append(stringified)
        scores.append(score(grid))
        north(grid)
        west(grid)
        south(grid)
        east(grid)
        stringified = "".join(["".join(line) for line in grid])
        try:
            offset = prev_grids.index(stringified)
            cycle_size = len(prev_grids) - offset
            break
        except ValueError:
            ...
    return scores[offset + (10**9 - offset) % cycle_size]


if __name__ == "__main__":
    with open("input.txt", "r") as f:  # your file here
        input = f.read().splitlines()
        print(part1(input))
        print(part2(input))
