#! python3
from math import prod

def initialize():
    with open('input-Day13.txt') as f:
        lines = f.readlines()

    earliest = int(lines[0].strip())
    buses = lines[1].strip().split(',')
    return earliest, buses


def part1(earliest, buses):
    bus_ids = [int(x) for x in buses if x.isnumeric()]
    print(bus_ids)
    diffs = []
    for id in bus_ids:
        factor = earliest // id
        num = id * ((earliest // id) + 1)
        diffs.append(num - earliest)

    print(diffs)
    index_of_min = diffs.index(min(diffs))
    print(bus_ids[index_of_min] * min(diffs))
    return bus_ids


def find_match(ids, offsets, index, inc, start):
    t = start
    check = []
    while len(check) < len(ids):
        t += inc
        check_times = [t + offset for offset in offsets]
        combs = zip(check_times, ids)
        check = list(filter(lambda x: x[0] % x[1] == 0, combs))
    new_increment = prod(ids)
    return t, new_increment


def part2(bus_ids, buses):
    offsets = [buses.index(str(x)) for x in bus_ids]
    check = []
    increment = 1
    timestamp = 0
    for i in range(2, len(bus_ids)+1):
        timestamp, increment = find_match(bus_ids[:i], offsets[:i], i, increment, timestamp)
    return timestamp


if __name__ == '__main__':
    earliest, buses = initialize()
    ids = part1(earliest, buses)
    t = part2(ids, buses)
    print(t)

