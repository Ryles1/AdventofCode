import heapq, time
from math import floor
from collections import deque


def get_adjacent(adjustment, location):
	new_row = location[0] + adjustment[0]
	new_col = location[1] + adjustment[1]
	return new_row, new_col


def parse_connections(matrix):
	adjacency_dict = {}
	max_row = len(matrix)
	max_col = len(matrix[0])
	adjustments = [(0, 1), (0, -1), (-1, 0), (1, 0)]
	for i, row in enumerate(matrix):
		for j, col in enumerate(row):
			adjacency_dict[(i, j)] = {}
			for adjustment in adjustments:
				adjacent = get_adjacent(adjustment, (i, j))
				if 0 <= adjacent[0] < max_row and 0 <= adjacent[1] < max_col:
					adjacency_dict[(i, j)][adjacent] = matrix[adjacent[0]][adjacent[1]]
	return adjacency_dict


def blank_costs(nodes, start):
	cost_dict = dict()
	for node in nodes:
		cost_dict[node] = 0 if node == start else float('inf')
	return cost_dict


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

		for next_node in adjacents[current].keys():
			new_cost = cost[current] + adjacents[current][next_node]
			if next_node not in cost or new_cost < cost[next_node]:
				cost[next_node] = new_cost
				frontier.append(next_node)
				came_from[next_node] = current

	return cost, came_from


def get_path(dirs, start, end):
	current = end
	path = []
	while current != start:
		path.append(str(current))
		current = dirs[current]
	path.append(str(start))
	path.reverse()
	return path


def heuristic(current, target):
	# manhattan distance
	distance_to_target = abs(target[0] - current[0]) + abs(target[1] - current[1])
	return distance_to_target


def a_star_costs_and_path(adjacents, start, end):
	frontier = [[0,start]]
	came_from = dict()
	came_from[start] = None
	cost = dict()
	cost[start] = 0
	while frontier:
		heapq.heapify(frontier)
		current_cost, current = heapq.heappop(frontier)

		if current == end:
			break

		for next_node in adjacents[current].keys():
			new_cost = cost[current] + adjacents[current][next_node]
			if next_node not in cost or new_cost < cost[next_node]:
				cost[next_node] = new_cost
				priority = new_cost + heuristic(next_node, end)
				heapq.heappush(frontier, [priority, next_node])
				came_from[next_node] = current

	return cost, came_from


def visualize(path, risk_map):
	for y, row in enumerate(risk_map):
		row_s = []
		for x, col in enumerate(row):
			if str((y, x)) in path:
				row_s.append('#')
			else:
				row_s.append('.')
		print(''.join(row_s))
	return


def get_lowest_risk(risk_map, start, end):
	# dict of format { (0, 0): {(0, 1): risk value} } to track each node's neighbors
	adjacency = parse_connections(risk_map)
	# dict of format {(0, 0): {(0, 1): risk value} to track total risk from start
	start = start
	end = end
	dijkstra_start = time.time()
	costs, directions = dijkstra_costs_and_path(adjacency, start, end)
	dijkstra_end = time.time()
	print(f'Dijkstra cost: {costs[end]}')
	lowest_cost_path = get_path(directions, start, end)
	print(f'Dijkstra time: {dijkstra_end - dijkstra_start}')
	a_star_start = time.time()
	a_star_cost, a_star_directions = a_star_costs_and_path(adjacency, start, end)
	a_star_end = time.time()
	a_star_path = get_path(a_star_directions, start, end)
	print(f'A* cost: {a_star_cost[end]}')
	print(f'A* time: {a_star_end - a_star_start}')
	return costs[end]


if __name__ == '__main__':
	FILENAME = './input/day15.txt'
	with open(FILENAME) as f:
		s = f.readlines()
		risk_map = [[int(i) for i in line.strip()] for line in s]

	tile_width = len(risk_map[0])
	tile_height = len(risk_map)
	START = (0, 0)
	END = (tile_height - 1, tile_width - 1)
	print(get_lowest_risk(risk_map, START, END))

	big_width = tile_width * 5
	big_height = tile_height * 5
	big_map = [[] for y in range(big_height)]
	for y in range(big_height):
		for x in range(big_width):
			x_translate = floor(x / tile_width)
			y_translate = floor(y / tile_height)
			risk = risk_map[y % tile_height][x % tile_width]
			risk_translate = (risk + x_translate + y_translate - 1) % 9 + 1
			big_map[y].append(risk_translate)

	END = (len(big_map) - 1, len(big_map[0]) - 1)
	#  Gives the right answer for A*, but not Dikstra for some reason
	#  on my input, Dijkstra gives 2942, A* gives 2938
	# suspect an issue with the algorithm near the end
	print(get_lowest_risk(big_map, START, END))
