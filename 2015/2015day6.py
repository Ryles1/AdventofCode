OFF = 0
ON = 1
SIZE = 1000


def parse_instruction(string):
    parts = string.split()
    if len(parts) == 4:
        command = parts[0]
        i = 1
    else:
        command = parts[1]
        i = 2
    topleft = parts[i].split(',')
    bottomright = parts[i + 2].split(',')
    tlx, tly = int(topleft[0]), int(topleft[1])
    brx, bry = int(bottomright[0]), int(bottomright[1])
    return command, tlx, tly, brx, bry


def count_lights(grid):
    return sum([sum(x) for x in grid])


def part1(instructions, size=SIZE):
    grid = [[OFF for __ in range(size)] for _ in range(size)]
    for instruction in instructions:
        command, top_left_y, top_left_x, bottom_right_y, bottom_right_x = parse_instruction(instruction)
        for y in range(top_left_y, bottom_right_y + 1):
            for x in range(top_left_x, bottom_right_x + 1):
                if command == 'on':
                    grid[y][x] = ON
                elif command == 'off':
                    grid[y][x] = OFF
                else:
                    grid[y][x] = ON if grid[y][x] == OFF else OFF
    lights_on = count_lights(grid)
    return lights_on


def part2(instructions, size=SIZE):
    grid = [[OFF for __ in range(size)] for _ in range(size)]
    for instruction in instructions:
        command, top_left_y, top_left_x, bottom_right_y, bottom_right_x = parse_instruction(instruction)
        for y in range(top_left_y, bottom_right_y + 1):
            for x in range(top_left_x, bottom_right_x + 1):
                if command == 'on':
                    grid[y][x] += 1
                elif command == 'off':
                    grid[y][x] -= 1
                    if grid[y][x] < 0:
                        grid[y][x] = 0
                else:
                    grid[y][x] += 2
    lights_on = count_lights(grid)
    return lights_on

if __name__ == '__main__':
    with open('day6.txt') as f:
        lines = f.read().split('\n')
    print(part1(lines))
    print(part2(lines))
