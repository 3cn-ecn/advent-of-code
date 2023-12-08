import re
from math import lcm


def part1(input: list[str]) -> int:
    path = input[0]
    graph = {}
    # init graph
    for line in input[2:]:
        tokens = re.search(r"(.*) = \((.*), (.*)\)", line)
        if tokens:
            graph[tokens.groups()[0]] = tokens.groups()[1:]

    index_ = 0
    curr = "AAA"
    while curr != "ZZZ":
        curr = graph[curr][int(path[index_ % len(path)] == "R")]
        index_ += 1
    return index_


def part2(input: list[str]) -> int:
    path = input[0]
    graph = {}
    currs = []
    # init graph
    for line in input[2:]:
        tokens = re.search(r"(.*) = \((.*), (.*)\)", line)
        if not tokens:
            continue
        key = tokens.groups()[0]
        graph[key] = tokens.groups()[1:]
        if tokens.groups()[0][2] == "A":
            currs.append(key)

    index_ = 0
    not_finished = True
    path_length = [0 for _ in range(len(currs))]
    while not_finished:
        not_finished = False
        for i, curr in enumerate(currs):
            if path_length[i] > 0:
                continue

            if curr[2] == "Z":
                path_length[i] = index_

            else:
                not_finished = True
                currs[i] = graph[curr][int(path[index_ % len(path)] == "R")]
        index_ += 1
    return lcm(*path_length)


if __name__ == "__main__":
    with open("input.txt", "r") as f:  # your file here
        input = f.read().splitlines()
        print(part1(input))
        print(part2(input))
