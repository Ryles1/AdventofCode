def parse(s):
    if s == 'noop':
        instruction = 'noop'
        value = 0
    else:
        instruction = s.split()[0]
        value = int(s.split()[1])
    return instruction, value


def part1(lines):
    cycle = 0
    X = 1
    signal_strengths = []
    cycles_to_inspect = [20, 60, 100, 140, 180, 220]
    for line in lines:
        if len(signal_strengths) == len(cycles_to_inspect):
            break
        instruction, value = parse(line.strip())
        if instruction == 'noop':
            cycle += 1
            if cycle in cycles_to_inspect:
                signal_strengths.append((cycle, X))
            continue
        else:
            cycle += 1
            if cycle in cycles_to_inspect:
                signal_strengths.append((cycle, X))
            cycle += 1
            if cycle in cycles_to_inspect:
                signal_strengths.append((cycle, X))
            X += value
    signal_strength = sum(x*y for x, y in signal_strengths)
    return signal_strength



if __name__ == '__main__':
    FILENAME = './input/day10.txt'
    with open(FILENAME) as f:
        lines = f.readlines()


    print(part1(lines))
    #print(part2(lines))