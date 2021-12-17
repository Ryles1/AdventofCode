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
	def __init__(self, name):
		self.name = name
		if name.islower():
			self.isSmall = True
		else:
			self.isSmall = False
		self.connections = []


def parse_connections(lines):
	node_list = NodeList()
	for line in lines:
		first, second = line.split('-')
		if first not in node_list.get_names():
			node_list.add_node(first)
		if second not in node_list.get_names():
			node_list.add_node(second)

	for line in lines:
		first, second = line.split('-')
		first_node = node_list.find_by_name(first)
		second_node = node_list.find_by_name(second)
		first_node.connections.append(second_node)
		second_node.connections.append(first_node)

	return node_list


def get_path(current_path, found_paths):
	current_node = current_path[-1]
	for connection in current_node.connections:
		if connection.name == 'end':
			found_paths.append(current_path + [connection])
		elif connection not in current_path:
			found_paths = get_path(current_path + [connection], found_paths)
		elif connection.isSmall or connection.name == 'start':
			pass
		else:
			current_path.append(connection)
			found_paths = get_path(current_path, found_paths)
	return found_paths


def part1(lines):
	nodes = parse_connections(lines)
	start = nodes.find_by_name('start')
	assert start is not None
	paths = []
	paths = get_path([start], paths)
	for path in paths:
		for node in path:
			print(','.join(node.name))
	return len(paths)


if __name__ == '__main__':
	FILENAME = './input/day12.txt'
	with open(FILENAME) as f:
		lines = f.read().strip().split('\n')

	print(part1(lines))
	#print(polymer_insertion(template, rule_lines, 40))
