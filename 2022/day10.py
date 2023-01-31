LIT = '#'
DARK = '.'

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


def part2(lines):
    cycle = 1
    sprite_center = 1
    screen = [[DARK for _ in range(40)] for _ in range(6)]
    row = 0
    for line in lines:
        row = (cycle // 40) - 1 if cycle > 40 else 0
        sprite_values = [sprite_center + adjustment for adjustment in (-1, 0, 1)]
        horizontal_location = cycle % 40 - 1
        instruction, value = parse(line.strip())
        if instruction == 'noop':
            if horizontal_location in sprite_values:
                screen[row][horizontal_location] = LIT
            cycle += 1
            continue
        else:
            row = (cycle // 40) - 1 if cycle > 40 else 0
            sprite_values = [sprite_center + adjustment for adjustment in (-1, 0, 1)]
            horizontal_location = cycle % 40 - 1
            if horizontal_location in sprite_values:
                screen[row][horizontal_location] = LIT
            cycle += 1
            row = (cycle // 40) - 1 if cycle > 40 else 0
            sprite_values = [sprite_center + adjustment for adjustment in (-1, 0, 1)]
            horizontal_location = cycle % 40 - 1
            if horizontal_location in sprite_values:
                screen[row][horizontal_location] = LIT
            cycle += 1
        sprite_center += value
    return screen



if __name__ == '__main__':
    FILENAME = './input/day10.txt'
    with open(FILENAME) as f:
        lines = f.readlines()

    print(part1(lines))
    screen = part2(lines)
    for row in screen:
        print(''.join(row))
