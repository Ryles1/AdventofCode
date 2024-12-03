from collections import Counter

def parse_lines(lines):
    list1 = []
    list2 = []
    for line in lines:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))
    list1.sort(), list2.sort()
    return list1, list2


def main1(lines):
    list1, list2 = parse_lines(lines)
    diffs = []
    for i, v in enumerate(list1):
        diffs.append(abs(list1[i] - list2[i]))
    return sum(diffs)


def main2(lines):
    list1, list2 = parse_lines(lines)
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    similarity = 0
    for i, v in enumerate(counter1):
        temp = v * counter2[v]
        similarity += temp
    return similarity


if __name__ == '__main__':
    with open('./input/day1.txt') as f:
        lines = f.read().strip().split('\n')

    answer1 = main1(lines)
    print(answer1)

    answer2 = main2(lines)
    print(answer2)