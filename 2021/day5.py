import copy


def parse_instructions(str):
	points = str.strip().split(' -> ')
	startx, starty = list(map(int, points[0].split(',')))
	endx, endy = list(map(int, points[1].split(',')))
	return startx, starty, endx, endy


def get_grid():
	new = []
	for i in range(1000):
		new.append([])
		for j in range(1000):
			new[i].append(0)
	return new


def get_vert_horz_vents(x1, y1, x2, y2, g):
	new_g = {}
	xmin = min([x1, x2])
	xmax = max([x1, x2])
	ymin = min([y1, y2])
	ymax = max([y1, y2])
	for x in range(xmin, xmax + 1):
		for y in range(ymin, ymax + 1):
			new_g[(x, y)] = 1
	return new_g


def count_overlaps(g):
	count = 0
	for v in g.values():
		if v > 1:
			count += 1
	return count


def get_diagonal_vents(x1, y1, x2, y2, g):
	new_g = {}
	x = x1
	y = y1
	while x != x2 and y != y2:
		new_g[(x, y)] = 1
		x += 1 if x2 > x1 else -1
		y += 1 if y2 > y1 else -1
	new_g[(x2, y2)] = 1
	return new_g


def vents(lines, part1):
	grid = {}
	for i, line in enumerate(lines):
		x1, y1, x2, y2 = parse_instructions(line)
		if part1 and not ((x1 == x2) or (y1 == y2)):
			continue

		if (x1 == x2) or (y1 == y2):
			new_grid = get_vert_horz_vents(x1, y1, x2, y2, grid)
		else:
			new_grid = get_diagonal_vents(x1, y1, x2, y2, grid)

		for key in new_grid.keys():
			if grid.get(key):
				grid[key] += 1
			else:
				grid[key] = 1
	count = count_overlaps(grid)
	return count


if __name__ == '__main__':
	FILENAME = './input/day5.txt'
	with open(FILENAME) as f:
		vent_lines = f.readlines()

	print(vents(vent_lines, True))
	print(vents(vent_lines, False))
