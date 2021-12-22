EMPTY = '.'
DOT = '#'


def get_new_matrix(xmax, ymax):
	new = []
	for y in range(ymax + 1):
		new.append([])
		for x in range(xmax + 1):
			new[y].append(EMPTY)
	return new


def populate_dots(dot_coords, matrix):
	for x, y in dot_coords:
		matrix[y][x] = DOT
	return matrix


def check_line_is_empty(direction, value, grid):
	isEmpty = False
	if direction == 'y':
		check_line = grid[value]
		isEmpty = all(filter(lambda i: i == EMPTY, check_line))
	if direction == 'x':
		check_line = [row[value] for row in grid]
		isEmpty = all(filter(lambda i: i == EMPTY, check_line))
	return isEmpty


def count_dots(grid):
	count = 0
	for row in grid:
		for col in row:
			count += 1 if col == DOT else 0
	return count


def foldy(value, grid):
	top_half = grid[:value]
	bottom_half = grid[value + 1:]
	bottom_flipped = bottom_half[::-1]
	assert len(top_half) == len(bottom_half), 'top and bottom are not the same length'
	new = []
	for i, row in enumerate(top_half):
		new.append([])
		for j in range(len(top_half[i])):
			if top_half[i][j] == DOT or bottom_flipped[i][j] == DOT:
				new[i].append(DOT)
			else:
				new[i].append(EMPTY)
	return new


def foldx(value, grid):
	left_half = []
	right_half = []
	for i, row in enumerate(grid):
		left_half.append([])
		right_half.append([])
		for j, col in enumerate(row):
			if j < value:
				left_half[i].append(col)
			elif j > value:
				right_half[i].append(col)
	right_half_flipped = [row[::-1] for row in right_half]
	assert len(left_half) == len(right_half), 'left and right are not the same length'
	new = []
	for i, row in enumerate(left_half):
		new.append([])
		for j in range(len(left_half[i])):
			if left_half[i][j] == DOT or right_half_flipped[i][j] == DOT:
				new[i].append(DOT)
			else:
				new[i].append(EMPTY)
	return new


def solve1(lines, instructions):
	xs = [int(line.split(',')[0]) for line in lines]
	ys = [int(line.split(',')[1]) for line in lines]
	xmax = int(instructions[0][-3:]) * 2
	ymax = int(instructions[1][-3:]) * 2
	dots = [(x, y) for x, y in zip(xs, ys)]
	paper = get_new_matrix(xmax, ymax)
	paper = populate_dots(dots, paper)
	for instruction in instructions:
		fold = instruction.split()[2]
		direction, fold_line = fold.split('=')
		fold_line = int(fold_line)
		if direction == 'x':
			assert check_line_is_empty(direction, fold_line, paper)
			paper = foldx(fold_line, paper)
			print(count_dots(paper))
		elif direction == 'y':
			assert check_line_is_empty(direction, fold_line, paper)
			paper = foldy(fold_line, paper)
			print(count_dots(paper))
	for row in paper:
		print()
		for col in row:
			print(col, end='', sep=' ')
	return


if __name__ == '__main__':
	FILENAME = './input/day13.txt'
	with open(FILENAME) as f:
		s = f.read().split('\n\n')
	lines = s[0].split('\n')
	instructions = s[1].split('\n')

	solve1(lines, instructions)
