def count_visited_positions(motions):
    head = (0, 0)
    tail = (0, 0)
    visited = set([(0, 0)])

    for motion in motions:
        direction = motion[0]
        steps = int(motion[1:])

        for _ in range(steps):
            if direction == 'R':
                head = (head[0] + 1, head[1])
            elif direction == 'L':
                head = (head[0] - 1, head[1])
            elif direction == 'U':
                head = (head[0], head[1] + 1)
            elif direction == 'D':
                head = (head[0], head[1] - 1)

            if abs(head[0] - tail[0]) + abs(head[1] - tail[1]) > 1:
                # Update tail position if head and tail are not adjacent
                if head[0] > tail[0]:
                    tail = (tail[0] + 1, tail[1])
                elif head[0] < tail[0]:
                    tail = (tail[0] - 1, tail[1])
                elif head[1] > tail[1]:
                    tail = (tail[0], tail[1] + 1)
                elif head[1] < tail[1]:
                    tail = (tail[0], tail[1] - 1)

            visited.add(tail)

    return len(visited)


if __name__ == '__main__':
    FILENAME = './input/day9.txt'
    with open(FILENAME) as f:
        lines = f.readlines()
    instructions = [[(direction, int(distance)) for direction, distance in line.split()] for line in lines]

    print(count_visited_positions(instructions))
    #print(part2(lines))