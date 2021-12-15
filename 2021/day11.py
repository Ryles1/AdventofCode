import copy, time
from collections import deque
MAX_ENERGY = 9


def get_neighbors(row, column, grid):
	"""Returns a list of neighbors inside the grid."""
	max_row = len(grid)
	max_col = len(grid[0])
	possible_neighbors = []
	# populate the (row, col) of all adjacent locations - no diagonals though
	for i in range(row - 1, row + 2):
		for j in range(column - 1, column + 2):
			if i == row and j == column:
				continue
			possible_neighbors.append((i, j))
	# x below is a (row, col) tuple for neighbors around the location in question
	# filter is used to avoid IndexErrors from going outside the matrix edges
	neighbors = list(filter(lambda x: 0 <= x[0] < max_row and 0 <= x[1] < max_col, possible_neighbors))
	return neighbors


def increase_energy(grid):
	new_grid = [[x + 1 for x in row] for row in grid]
	return new_grid


def check_for_flashes(grid, flashed=None):
	"""This function finds all locations on the grid that have value greater than 9 and have not already flashed
	in this step."""
	if flashed is None:
		flashed = list()
	flashed_locations = deque()
	for i, row in enumerate(grid):
		for j, col in enumerate(row):
			if grid[i][j] > MAX_ENERGY and not (i, j) in flashed:
				flashed_locations.append((i, j))
	return flashed_locations


def reset_flashes(grid):
	new_grid = []
	for i, row in enumerate(grid):
		new_grid.append([])
		for j, col in enumerate(row):
			if col > 9:
				new_grid[i].append(0)
			else:
				new_grid[i].append(col)
	return new_grid


def update_for_flash(grid, current, neighbors):
	new_grid = []
	for i, row in enumerate(grid):
		new_grid.append([])
		for j, col in enumerate(row):
			if (i, j) in neighbors:
				new_grid[i].append(grid[i][j] + 1)
			else:
				new_grid[i].append(grid[i][j])
	return new_grid


def part1(grid, steps):
	total_flashes = 0
	flashes = deque()
	for step in range(steps):
		flashed_grid = []
		flashed_this_step = []
		# increase energy levels by one
		updated_grid = increase_energy(grid)
		# get a deque of (x, y) tuples of octopi that flashed
		flashes = check_for_flashes(updated_grid, flashes)
		#track octopi that have flashed this step
		flashed_this_step.extend(list(flashes))
		# handle each flash - since a flash can cause adjacent octopi to flash, run until the deque is empty
		while len(flashes) > 0:
			flash = flashes.popleft()
			neighbors = get_neighbors(flash[0], flash[1], updated_grid)
			flashed_grid = update_for_flash(updated_grid, flash, neighbors)
			# check for new flashes
			new_flashes = check_for_flashes(flashed_grid, flashed_this_step)
			flashes.extend(new_flashes)
			flashed_this_step.extend(list(new_flashes))
			updated_grid = copy.deepcopy(flashed_grid)

		# reset flashed octopi to energy level 0
		final_grid = reset_flashes(flashed_grid)
		total_flashes += len(flashed_this_step)
		if final_grid:
			grid = copy.deepcopy(final_grid)
		else:
			grid = copy.deepcopy(updated_grid)
	return total_flashes


def check_all_flashed(grid):
	for y in grid:
		for x in y:
			if x != 0:
				return False
	return True


def part2(grid):
	steps = 0
	all_flashed = False
	flashes = deque()
	start = time.time()
	while not all_flashed:
		steps += 1
		print(f'Step: {steps}')
		flashed_grid = []
		flashed_this_step = []
		# increase energy levels by one
		updated_grid = increase_energy(grid)
		# get a deque of (x, y) tuples of octopi that flashed
		flashes = check_for_flashes(updated_grid, flashes)
		#track octopi that have flashed this step
		flashed_this_step.extend(list(flashes))
		# handle each flash - since a flash can cause adjacent octopi to flash, run until the deque is empty
		while len(flashes) > 0:
			flash = flashes.popleft()
			print(f'Checking {flash}')
			neighbors = get_neighbors(flash[0], flash[1], updated_grid)
			flashed_grid = update_for_flash(updated_grid, flash, neighbors)
			# check for new flashes
			new_flashes = check_for_flashes(flashed_grid, flashed_this_step)
			flashes.extend(new_flashes)
			flashed_this_step.extend(list(new_flashes))
			updated_grid = copy.deepcopy(flashed_grid)
		# reset flashed octopi to energy level 0
		final_grid = reset_flashes(flashed_grid)

		if final_grid:
			grid = copy.deepcopy(final_grid)
		else:
			grid = copy.deepcopy(updated_grid)

		all_flashed = check_all_flashed(grid)
		end = time.time()
		if (end - start) > 60:
			break
	return steps


if __name__ == '__main__':
	FILENAME = './input/day11.txt'
	with open(FILENAME) as f:
		lines = f.readlines()
	lines = [line.strip() for line in lines]

	octopi = [[int(x) for x in row] for row in lines]
	print(part1(octopi, 100))
	print(part2(octopi))

