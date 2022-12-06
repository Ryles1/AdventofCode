def part1(lines):
    full_overlaps = 0
    for line in lines:
        range1, range2 = line.split(',')
        start1, end1 = [int(i) for i in range1.split('-')]
        start2, end2 = [int(j) for j in range2.split('-')]
        sectionSet1 = set(range(start1, end1 + 1))
        sectionSet2 = set(range(start2, end2 + 1))
        # check for subsets of each other
        if sectionSet2.issubset(sectionSet1) or sectionSet1.issubset(sectionSet2):
            full_overlaps += 1
    return full_overlaps


def part2(lines):
    partial_overlaps = 0
    for line in lines:
        range1, range2 = line.split(',')
        start1, end1 = [int(i) for i in range1.split('-')]
        start2, end2 = [int(j) for j in range2.split('-')]
        sectionSet1 = set(range(start1, end1 + 1))
        sectionSet2 = set(range(start2, end2 + 1))
        # check for partial overlap by checking for intersections existing
        if sectionSet2.intersection(sectionSet1):
            partial_overlaps += 1
    return partial_overlaps


if __name__ == '__main__':
    with open('./input/day4.txt') as f:
        lines = f.readlines()

    print(part1(lines))
    print(part2(lines))