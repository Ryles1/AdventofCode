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
    topleft = parts[i].split(",")
    bottomright = parts[i + 2].split(",")
    tlx, tly = topleft[0], topleft[1]
    brx, bry = bottomright[0], bottomright[1]
    return command, tlx, tly, brx, bry


def count_lights(grid):
    return sum([sum(x) for x in grid])


def toggle_row(x1, x2, grid):
    current_row = grid[x1 : x2 + 1]
    for x, v in enumerate(current_row):
        current_row[x] = OFF if current_row[x] == ON else ON


# function for turning on a row? or off an entire row?


def part1(size=SIZE):
    with open("./input/2015day6input.txt") as f:
        instructions = f.readlines()

    grid = [[OFF] * size] * size
    for instruction in instructions:
        (
            command,
            top_left_x,
            top_left_y,
            bottom_right_x,
            bottom_right_y,
        ) = parse_instruction(instruction)
    if command == "toggle":
        for row in range(top_left_y, bottom_right_y + 1):
            toggle_row(top_left_x, bottom_right_x)
    lights_on = count_lights(grid)
    return lights_on


print(part1())
