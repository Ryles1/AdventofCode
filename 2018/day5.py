def isSameType(pair):
    return pair[0].lower() == pair[1].lower()


def isOppPolarity(pair):
    if pair[0] == pair[0].lower():
        if pair[1] == pair[1].upper():
            return True
    if pair[0] == pair[0].upper():
        if pair[1] == pair[1].lower():
            return True
    return False


def main(s):
    polymer = list(s)
    i = 0
    while i < len(polymer) - 1:
        window = polymer[i:i + 2]
        if isSameType(window) and isOppPolarity(window):
            del polymer[i+1]
            del polymer[i]
            i -= 1 if i > 0 else 0
            continue
        i += 1
    backwards = list(reversed(polymer))
    return len(polymer)


if __name__ == '__main__':
    with open('./input/day5.txt') as f:
        s = f.read().strip()

    ans1 = main(s)
    print(ans1)
