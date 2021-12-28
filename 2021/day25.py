import copy
EAST = '>'
SOUTH = 'v'
EMPTY = '.'


def get_grid(cucumber_lines):
	grid = [[c for c in row] for row in cucumber_lines]
	return grid


def get_moves(g, direction):
	moves = []
	for i, row in enumerate(g):
		for j, col in enumerate(row):
			if col == direction and direction  == EAST:
				if j + 1 == len(row):
					if g[i][0] == '.':
						moves.append((i, j))
				elif g[i][j + 1] == '.':
					moves.append((i, j))
			elif col == direction and direction == SOUTH:
				if i + 1 == len(g):
					if g[0][j] == '.':
						moves.append((i, j))
				elif g[i + 1][j] == '.':
					moves.append((i, j))
	return moves


def update_moves(g, moves, direction):
	new_grid = copy.deepcopy(g)
	for i, j in moves:
		if direction == EAST:
			if j + 1 == len(g[i]):
				new_grid[i][j] = EMPTY
				new_grid[i][0] = EAST
			else:
				new_grid[i][j] = EMPTY
				new_grid[i][j+1] = EAST
		elif direction == SOUTH:
			if i + 1 == len(g):
				new_grid[i][j] = EMPTY
				new_grid[0][j] = SOUTH
			else:
				new_grid[i][j] = EMPTY
				new_grid[i+1][j] = SOUTH
	return new_grid


def main(lines):
	cucumbers = [line for line in lines.split('\n')]
	cucumber_grid = get_grid(cucumbers)
	cucumber_moved = True
	steps = 0
	while cucumber_moved:
		east_moves = get_moves(cucumber_grid, EAST)
		cucumber_grid = update_moves(cucumber_grid, east_moves, EAST)
		south_moves = get_moves(cucumber_grid, SOUTH)
		cucumber_grid = update_moves(cucumber_grid, south_moves, SOUTH)

		if len(east_moves) == 0 and len(south_moves) == 0:
			steps += 1
			cucumber_moved = False
		else:
			steps += 1
			print(steps)

	return steps


if __name__ == '__main__':
	FILENAME = '.\input\day25.txt'
	with open(FILENAME) as f:
		lines = f.read().strip()

	print(main(lines))
