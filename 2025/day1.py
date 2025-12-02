def main1(instructions, start=50):
    zeros = 0
    current = start
    for instr in instructions:
        new = current
        dirn, num = instr[0], int(instr[1:])
        if num > 100:
            num %= 100
        if dirn == 'L':
            if num <= current:
                new = current - num
            elif num > current:
                diff = num - current
                new = 100 - diff
        elif dirn == 'R':
            if (num + current) <= 99:
                new = current + num
            elif (num + current) >= 100:
                new = current + num - 100
        current = new
        current = 0 if current == 100 else current
        zeros += 1 if current == 0 else 0
    return zeros


def main2(instructions, start=50):
    zeros = 0
    current = start
    for instr in instructions:
        new = current
        dirn, num = instr[0], int(instr[1:])
        if num >= 100:
            zeros += num // 100
            num %= 100
        if dirn == 'L':
            if num <= current:
                new = current - num
                zeros += 1 if new == 0 else 0
            elif num > current:
                diff = num - current
                new = 100 - diff
                zeros += 1 if current != 0 else 0 #prevent double counting if counter is already at 0
        elif dirn == 'R':
            if (num + current) < 100:
                new = current + num
            elif (num + current) >= 100:
                new = current + num - 100
                zeros += 1 if current != 0 else 0  #prevent double counting if counter is already at 0
        current = new

    return zeros


if __name__ == '__main__':
    with open('./input/day1.txt') as f:
        lines = f.read().splitlines()

    answer1 = main1(lines)
    print(answer1)

    print(main2(lines))
