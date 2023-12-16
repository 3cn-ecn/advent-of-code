class Map:
    def __init__(self):
        self.interval_src = []
        self.interval_dst = []
        self.length = 0

    def append(self, start_src: int, start_dst: int, range_length: int):
        self.interval_src.append((start_src, start_src + range_length))
        self.interval_dst.append(start_dst)
        self.length += 1

    def correspondance(self, value: int) -> int:
        for i in range(len(self.interval_src)):
            if self.interval_src[i][0] <= value < self.interval_src[i][1]:
                return self.interval_dst[i] + value - self.interval_src[i][0]

        return value


# PART 1

def part1(input_: [str]) -> int:
    maps = [Map() for _ in range(7)]
    seeds = list(map(int, input_[0].replace('\n', '').split(": ")[1].split(' ')))
    i = -1

    for line in input_[1:]:
        if line == '\n':
            i += 1
        elif line[0].isdigit():
            converted_list = list(map(int, line.replace('\n', '').split(' ')))
            maps[i].append(converted_list[1], converted_list[0], converted_list[2])

    min_location = float("inf")

    for i in seeds:
        for j in range(7):
            i = maps[j].correspondance(i)

        if min_location > i:
            min_location = i

    return min_location


# PART 2
#
# GENERAL PRINCIPLE
# 
# Instead of calculating each value in each intervals (calculating time skyrocketing), I treat each interval with its endpoints. But the maps might not 
# respect the endpoints of an interval, so one interval might be divided in smaller intervals (but their union is still equal to the first interval).
# At the end, the smallest inferior endpoint is the answer.
#
# All of this is possible because the maps represent 1-slope linear function.

def part2(input_: [str]) -> int:
    def evolv(intervals: [(int, int)], maps: Map) -> [[(int, int)], [(int, int)]]:
        # We keep track of which intervals are modified by maps because modified intervals should not be changed another map, but modified ones must.

        modified_intervals = []
        unmodified_intervals = []

        for i in range(len(intervals)):
            # Both maps' endpoints are in intervals[i]
            if intervals[i][0] <= maps[1] < intervals[i][1] and intervals[i][0] <= maps[1] + maps[2] < intervals[i][1]:
                modified_intervals.append((maps[0], maps[0] + maps[2]))
                unmodified_intervals += [(intervals[i][0], maps[1]), (maps[1] + maps[2], intervals[i][1])]
            # Only maps' inferior endpoint is in intervals[i]
            elif intervals[i][0] < maps[1] < intervals[i][1]:  
                modified_intervals.append((maps[0], maps[0] + intervals[i][1] - maps[1]))
                unmodified_intervals.append((intervals[i][0], maps[1]))
            # Only maps' superior endpoint is in intervals[i]
            elif intervals[i][0] < maps[1] + maps[2] < intervals[i][1]:  
                modified_intervals.append((maps[0] + intervals[i][0] - maps[1], maps[0] + maps[2]))
                unmodified_intervals.append((maps[1] + maps[2], intervals[i][1]))
            # intervals[i] is inside maps
            elif maps[1] <= intervals[i][0] and intervals[i][1] <= maps[1] + maps[2]: 
                modified_intervals += [(maps[0] + intervals[i][0] - maps[1], maps[0] + intervals[i][1] - maps[1])]
            # The union of intervals[i] and maps is empty
            else: 
                unmodified_intervals.append(intervals[i])

        return modified_intervals, unmodified_intervals


    seeds = list(map(int, input_[0].replace('\n', '').split(": ")[1].split(' ')))
    intervals_to_scan = [(seeds[2*k], seeds[2*k] + seeds[2*k+1]) for k in range(len(seeds) // 2)]  # Interval (a, b) is a the mathematical interger interval [a; b[

    next_intervals = []  # Will contains intervals which were changed by a map in a section and must not be changed by another map of the section

    for line in input_[1:]:
        if line[0].isdigit():
            intervals_done, intervals_to_scan = evolv(intervals_to_scan, list(map(int, line.replace('\n', '').split(' '))))
            next_intervals += intervals_done
        elif line == '\n':  # Is True when line is the title of a section (e.g "humidity-to-location map:")
            intervals_to_scan += next_intervals  # All intervals which weren't modified my a map are merged with modified one
            next_intervals = []
            pass
            
    min_loc = float("inf")

    for x, _ in intervals_to_scan:
        if x < min_loc:
            min_loc = x

    return min_loc
