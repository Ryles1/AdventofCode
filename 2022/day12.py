from collections import deque


def get_neighbors(row, column, grid):
	"""Returns a list of neighbor nodes.
	This is done by obtaining first the indexes of the adjacent horizontal grid positions, then
	filtering them to ensure they are inside the grid (index must be greater than 0, less than the max row/col
	dimension).  The values for each neighbor are then obtained and the min value is compared to the value at the
	current grid location."""
	max_row = len(grid)
	max_col = len(grid[0])
	possible_neighbors = []
	# populate the (row, col) of all adjacent locations - no diagonals though
	for i in (row - 1, row + 1):
		possible_neighbors.append((i, column))
	for j in (column - 1, column + 1):
		possible_neighbors.append((row, j))
	# x below is a (row, col) tuple for neighbors around the location in question
	# filter is used to avoid IndexErrors from going outside the matrix edges
	neighbors = list(filter(lambda x: 0 <= x[0] < max_row and 0 <= x[1] < max_col, possible_neighbors))
	return neighbors


def get_adjacent(adjustment, location):
	new_row = location[0] + adjustment[0]
	new_col = location[1] + adjustment[1]
	return new_row, new_col


def parse_connections(matrix):
	# only returns connections that are at most 1 elevation higher than current node
	adjacency_dict = {}
	max_row = len(matrix)
	max_col = len(matrix[0])
	adjustments = [(0, 1), (0, -1), (-1, 0), (1, 0)]
	for i, row in enumerate(matrix):
		for j, col in enumerate(row):
			adjacency_dict[(i, j)] = {}
			current_height = col
			for adjustment in adjustments:
				adjacent = get_adjacent(adjustment, (i, j))

				if 0 <= adjacent[0] < max_row and 0 <= adjacent[1] < max_col:
					adjacent_height = matrix[adjacent[0]][adjacent[1]]
					if current_height == adjacent_height or adjacent_height <= (current_height + 1):
						adjacency_dict[(i, j)][adjacent] = matrix[adjacent[0]][adjacent[1]]
	return adjacency_dict


def dijkstra_costs_and_path(adjacents, start, end):
	frontier = deque((start,))
	came_from = dict()
	cost = dict()
	came_from[start] = None
	cost[start] = 0
	while not len(frontier) == 0:
		current = frontier.popleft()

		if current == end:
			break
		current_adjacents = adjacents[current].keys()
		for next_node in current_adjacents:
			# all steps cost 1
			new_cost = cost[current] + 1
			if next_node not in cost or new_cost < cost[next_node]:
				cost[next_node] = new_cost
				frontier.append(next_node)
				came_from[next_node] = current

	return cost, came_from


def dijkstra(hmap, start, end, part2=False):
	# dict of format { (0, 0): {(0, 1): risk value} } to track each node's neighbors
	adjacency = parse_connections(hmap)
	# dict of format {(0, 0): {(0, 1): risk value} to track total risk from start
	costs, directions = dijkstra_costs_and_path(adjacency, start, end)
	return costs


if __name__ == '__main__':
	FILENAME = './input/day12.txt'
	with open(FILENAME) as f:
		s = f.readlines()

	height_dict = {k: v for k, v in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}

	height_map = []
	for j, line in enumerate(s):
		row = []
		for i, v in enumerate(line.strip()):
			if v == 'S':
				start = (j, i)
				row.append(1)
				continue
			elif v == 'E':
				end = (j, i)
				row.append(26)
				continue
			else:
				row.append(height_dict[v])
		height_map.append(row)

	part1_costs = (dijkstra(height_map, start, end))
	print(f'Part 1 cost: {part1_costs[end]}')
	a_costs = []
	# run dijkstra for all 'a' starting locations
	for y, row in enumerate(height_map):
		for x, col in enumerate(row):
			if col == 1:
				try:
					a_cost = dijkstra(height_map, (y,x), end, True)
					a_costs.append(((y, x), a_cost[end]))
				except KeyError:
					continue
	sorted_costs = (sorted(a_costs, key=lambda p: p[1]))
	print(sorted_costs[0])
