def part1(s):
    for i in range(4, len(s)):
        window = s[i - 4: i]
        windowSet = set(window)
        if len(windowSet) == 4:
            return i


def part2(s):
    for i in range(14, len(s)):
        window = s[i - 14: i]
        windowSet = set(window)
        if len(windowSet) == 14:
            return i


if __name__ == '__main__':
    with open('./input/day6.txt') as f:
        raw = f.read().strip()


    print(part1(raw))
    print(part2(raw))
