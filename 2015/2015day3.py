# CONSTANTS
NORTH = "^"
SOUTH = "v"
EAST = ">"
WEST = "<"
d = {"^": -1, "v": 1, "<": -1, ">": 1}

# Collect input
with open("./input/2015day3input.txt") as f:
    directions = f.read()


def part1():
    # Initialize counters
    houses_unique = [(0, 0)]
    current_x = 0
    current_y = 0

    for dir in directions:
        if dir == NORTH or dir == SOUTH:
            current_y += d[dir]
        elif dir == EAST or dir == WEST:
            current_x += d[dir]
        # update santa's location and append to traveled locations if new
        new_location = (current_x, current_y)
        if new_location in houses_unique:
            pass
        else:
            houses_unique.append(new_location)

    print(len(houses_unique))


def part2():
    houses_unique = [(0, 0)]
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    # same as part 1, but track santa and robot separately
    for i, dir in enumerate(directions):
        x_update, y_update = 0, 0
        if dir == NORTH or dir == SOUTH:
            y_update += d[dir]
        elif dir == EAST or dir == WEST:
            x_update += d[dir]

        if i % 2 == 0:
            santa_x += x_update
            santa_y += y_update
            new_santa_location = (santa_x, santa_y)
            if new_santa_location in houses_unique:
                pass
            else:
                houses_unique.append(new_santa_location)
        else:
            robo_x += x_update
            robo_y += y_update
            new_robo_location = (robo_x, robo_y)
            if new_robo_location in houses_unique:
                pass
            else:
                houses_unique.append(new_robo_location)

    print(len(houses_unique))


if __name__ == "__main__":
    part1()
    part2()
