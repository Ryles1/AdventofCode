def rotate(start_dir, rotate_dir) -> int:
    """Facing direction is represented by values 0, 1, 2, and -1 arranged as below:
          0
      -1    1
          2
    This function takes in the starting direction and returns the direction after the
    rotation is applied."""
    end_dir = start_dir + 1 if rotate_dir == 'R' else start_dir - 1
    end_dir = -1 if end_dir == 3 else end_dir
    end_dir = 2 if end_dir == -2 else end_dir
    return end_dir


def translate(dir, blocks, current_location) -> tuple[int, int]:
    x, y = current_location
    if dir in (-1, 1):
        x += blocks * dir
    elif dir == 0:
        y += blocks
    elif dir == 2:
        y -= blocks
    else:
        raise
    return x, y


def calc_distance(loc):
    return abs(loc[0]) + abs(loc[1])


def get_path(start, end):
    """Function takes in two tuples representing the start and end coordinates of a straight line.
    Returns a list of tuples of all the locations on the line.
    The starting location is omitted to avoid duplicates in the 'visited' tracking list in main."""
    intersections = []
    x1, y1 = start
    x2, y2 = end
    if x1 == x2:
        x = x1
        ystart, yend = min(y1, y2), max(y1, y2)
        for y in range(ystart, yend+1):
            if (x, y) == start:
                continue
            intersections.append((x, y))
    elif y1 == y2:
        y = y1
        xstart, xend = min(x1, x2), max(x1, x2)
        for x in range(xstart, xend+1):
            if (x, y) == start:
                continue
            intersections.append((x, y))
    return intersections


def main(instructions):
    facing: int = 0
    start: tuple[int, int] = (0, 0)
    visited = [(0, 0)]  # initialize the list of visited locations
    first_duplicate = None
    distance2 = None
    for line in instructions:
        rotation, num_blocks = line[0], int(line[1:])
        facing = rotate(facing, rotation)
        end = translate(facing, num_blocks, start)
        path = get_path(start, end)
        if first_duplicate is None:  # looking for the first duplicate only
            for site in path:
                if site in visited:
                    first_duplicate = site
        visited.extend(path)
        start = end
    distance = calc_distance(start)
    distance2 = calc_distance(first_duplicate)
    return (distance, distance2)  # return sum of the blocks traveled in each direction


if __name__ == '__main__':
    with open('./input/day1.txt') as f:
        instructions = f.read().strip().split(',')
    instructions = [line.strip() for line in instructions]
    print(main(instructions))
