#! python3
from collections import deque

def initialize():
    with open('input-Day12.txt') as f:
        lines = f.read().strip().split('\n')
    return lines


def part1(directions):
    location = {'east':0, 'north':0}
    facing = deque('ESWN')
    for direction in directions:
        operation = direction[0]
        if direction.startswith('L'):
            steps = int(direction[1:].strip()) // 90
            facing.rotate(steps)
        elif direction.startswith('R'):
            steps = int(direction[1:].strip()) // 90
            facing.rotate(-steps)
        elif direction.startswith('E'):
            location['east'] += int(direction[1:].strip())
        elif direction.startswith('W'):
            location['east'] -= int(direction[1:].strip())
        elif direction.startswith('N'):
            location['north'] += int(direction[1:].strip())
        elif direction.startswith('S'):
            location['north'] -= int(direction[1:].strip())
        else:
            dir = facing[0]
            steps = int(direction[1:])
            if dir.startswith('E'):
                location['east'] += steps
            elif dir.startswith('W'):
                location['east'] -= steps
            elif dir.startswith('N'):
                location['north'] += steps
            elif dir.startswith('S'):
                location['north'] -= steps
            else:
                continue
    return sum([abs(y) for y in location.values()])


if __name__ == '__main__':
    instructions = initialize()
    manhattan = part1(instructions)
    print(manhattan)