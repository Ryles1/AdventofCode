SAND_START_X = 500
SAND_START_Y = 0
ROCK = '#'
SAND = 'o'
AIR = '.'


def get_rock_map_dict(scan):
    rocks = {}
    for line in scan:
        corners = line.split(' -> ')
        for i, corner in enumerate(corners[:-1]):
            start_x, start_y = [int(m) for m in corner.split(',')]
            end_x, end_y = [int(n) for n in corners[i+1].split(',')]
            # one of the diff's will be 0, apply both anyways for simplicity
            diff_y = end_y - start_y
            diff_x = end_x - start_x
            if diff_x > 0:
                combs = [(start_x + i, start_y) for i in range(diff_x + 1)]
            elif diff_x < 0:
                combs = [(start_x - i, start_y) for i in range(abs(diff_x) + 1)]
            elif diff_y > 0:
                combs = [(start_x, start_y + i) for i in range(diff_y + 1)]
            elif diff_y < 0:
                combs = [(start_x, start_y - i) for i in range(abs(diff_y) + 1)]
            for comb in combs:
                rocks[comb] = ROCK
    return rocks


def get_collision_row(m, sand, bottom):
    col = sand[1]
    collision_row = sand[0]
    # check every row between the sand and the bottom
    for row in range(collision_row, bottom):
        if m[row][col] == AIR:
            continue
        # if location is not open, then there's a collision
        else:
            collision_row = row
            return collision_row
    # if no collision occurs, return None
    return None


def print_map(m):
    for y in range(min(20, len(m))):
        print('\n')
        for x in range (480, min(520, len(m[y]))):
            print(m[y][x], sep='', end='')


def part1(m):
    bottom_row = len(m)
    sand_count = 0

    overflowing = False
    while not overflowing:
        current_sand = [SAND_START_Y, SAND_START_X]
        sand_count += 1
        falling = True
        while falling:
            next_collision_row = get_collision_row(m, current_sand, bottom_row)
            # if the sand goes below bottom of the map, break out of both loops
            if next_collision_row is None:
                # this sand doesn't count as it doesn't come to rest
                sand_count -= 1
                overflowing = True
                break
            current_sand[0] = next_collision_row - 1
            current_col = current_sand[1]
            # if sand moves over a column, repeat the falling step
            if m[next_collision_row][current_col - 1] == AIR:
                current_sand = [next_collision_row, current_col - 1]
            elif (current_col + 1) < len(m[next_collision_row]) and m[next_collision_row][current_col + 1] == AIR:
                current_sand = [next_collision_row, current_col + 1]
            else:
                m[next_collision_row - 1][current_col] = SAND
                falling = False
    with open('day14final.txt', 'w') as f:
        for line in m:
            f.write(''.join(line))
            f.write('\n')
    return sand_count


def get_rock_map_list(rock_map):
    xs = [x for x, y in rock_map.keys()]
    minx = min(xs)
    maxx = max(xs)
    ys = [y for x, y in rock_map.keys()]
    miny = min(ys)
    maxy = max(ys)
    rock_map_list = []
    # add an extra row and 5 additional columns to the map to avoid edge checks
    for y in range(maxy + 2):
        rock_map_list.append([])
        for x in range(maxx + 6):
            if (x, y) in rock_map.keys():
                rock_map_list[y].append(ROCK)
            else:
                rock_map_list[y].append(AIR)
    return rock_map_list


if __name__ == '__main__':
    FILENAME = './input/day14.txt'
    with open(FILENAME) as f:
        raw_scan = f.readlines()

    rock_map = get_rock_map_dict(raw_scan)
    rock_map1 = get_rock_map_list(rock_map)

    with open('day14map1.txt', 'w') as f:
        for line in rock_map1:
            f.write(''.join(line))
            f.write('\n')
    ans1 = part1(rock_map1)
    print(ans1)

    rock_map2 = rock_map1
    rock_map2.append([AIR for _ in range(len(rock_map2[0]))])
    rock_map2.append([ROCK for _ in range(len(rock_map2[0]))])


