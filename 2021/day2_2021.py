def part1(commands):
	"""The answer is the final depth multiplied by horizontal position.  This can be calculated by simply summing
	the commands given in the input and calculating the net depth."""
	horizontal_position = sum([int(command[-1]) for command in commands if command.startswith('f')])
	total_up = sum([int(command[-1]) for command in commands if command.startswith('u')])
	total_down = sum([int(command[-1]) for command in commands if command.startswith('d')])
	depth = total_down - total_up
	return horizontal_position * depth


def part2(instructions):
	horizontal_position, depth, aim = 0, 0, 0
	for instruction in instructions:
		value = int(instruction[-1])
		command = instruction.split()[0]
		if command == 'up':
			aim -= value
		elif command == 'down':
			aim += value
		elif command == 'forward':
			horizontal_position += value
			depth += (aim * value)

	return horizontal_position * depth


if __name__ == '__main__':
	with open('./input/day2.txt') as f:
		lines = f.read().split('\n')

	print(part1(lines))
	print(part2(lines))
