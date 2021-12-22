def get_new_matrix(size):
	new = []
	for x in range(size):
		new.append([])
		for y in range(size):
			new[x].append([])
			for z in range(size):
				new[x][y].append(0)
	return new


def parse_instruction(str):
	instruction, dim_str = str.split()
	dims = dim_str.split(',')
	dim_tuples = []
	for d in dims:
		nums = d[2:].split('..')
		dim_tuples.append((int(nums[0]) + 50, int(nums[1]) + 50))
	return instruction, dim_tuples


def cubes_on(g):
	count = 0
	for i in range(len(g)):
		for j in range(len(g[i])):
			for k in range(len(g[i][j])):
				count += g[i][j][k]
	return count


def perform_step(g, setting, cubes):
	value = 1 if setting == 'on' else 0
	for x in range(cubes[0][0], cubes[0][1] + 1):
		for y in range(cubes[1][0], cubes[1][1] + 1):
			for z in range(cubes[2][0], cubes[2][1] + 1):
				g[x][y][z] = value


def initialize(steps, size):
	grid = get_new_matrix(size)
	for i, step in enumerate(steps):
		if i > 19:
			break
		setting, cubes = parse_instruction(step)
		perform_step(grid, setting, cubes)
	on_count = cubes_on(grid)
	return on_count


if __name__ == '__main__':
	FILENAME = '.\input\day22.txt'
	with open(FILENAME) as f:
		L = f.readlines()
		lines = [l.strip() for l in L]


	print(initialize(lines, 100))