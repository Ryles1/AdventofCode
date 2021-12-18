from collections import Counter


class NodeList:
	def __init__(self):
		self.nodes = []

	def get_names(self):
		return [x.name for x in self.nodes]

	def get_nodes(self):
		return [node for node in self.nodes]

	def find_by_name(self, name):
		return self.nodes[self.get_names().index(name)]

	def add_node(self, name):
		self.nodes.append(Node(name))


class Node:
	"""This class represents each node in the grid.
	name: str
		'name' of the cave
	isLower: bool
		defines whether name is lowercase
	connections: list
		list of node elements representing caves that are connected to this node"""
	def __init__(self, name):
		self.name = name
		if name.islower():
			self.isSmall = True
		else:
			self.isSmall = False
		self.connections = []


def parse_connections(lines):
	node_list = NodeList()
	# populate the list of nodes
	for line in lines:
		first, second = line.split('-')
		if first not in node_list.get_names():
			node_list.add_node(first)
		if second not in node_list.get_names():
			node_list.add_node(second)

	# for each node, populate the connections
	for line in lines:
		first, second = line.split('-')
		first_node = node_list.find_by_name(first)
		second_node = node_list.find_by_name(second)
		first_node.connections.append(second_node)
		second_node.connections.append(first_node)

	return node_list


def smalls_in_path(path, num_repeats):
	"""return True if any small cave has already been visited at least 'num_repeats' times"""
	smalls = []
	for node in path:
		if node.isSmall:
			smalls.append(node)
	counter = Counter(smalls)
	if num_repeats in counter.values():
		return True
	return False


def get_path(current_path, found_paths, small_repeats=1):
	"""Recursive function to check each path and populate it in the found_paths list if it meets the criteria."""
	current_node = current_path[-1]  # check the last node in the current path
	for connection in current_node.connections:  #  for each connection of this node
		if connection.name == 'end':
			found_paths.append(current_path + [connection])
		elif connection.name == 'start':
			pass
		elif connection not in current_path:
			found_paths = get_path(current_path + [connection], found_paths, small_repeats)
		elif connection.isSmall:
			if not smalls_in_path(current_path, small_repeats):
				found_paths = get_path(current_path + [connection], found_paths, small_repeats)
		else:  # node is in the current path but is not small, so it can go in the path again
			found_paths = get_path(current_path + [connection], found_paths, small_repeats)
	return found_paths


def solve(lines):
	nodes = parse_connections(lines)
	start = nodes.find_by_name('start')
	assert start is not None
	paths1 = []
	paths1 = get_path([start], paths1)
	print(f'Part 1: {len(paths1)}')
	paths2 = []
	path2 = get_path([start], paths2, 2)
	print(f'Part 2: {len(paths2)}')


if __name__ == '__main__':
	FILENAME = './input/day12.txt'
	with open(FILENAME) as f:
		lines = f.read().strip().split('\n')

	print(solve(lines))
