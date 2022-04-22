#! python3

with open('input-Day8.txt') as f:
	inp = f.read().strip().split('\n')


def part_1(lines):
	acc = 0
	used_lines = []
	line = 0
	while line not in used_lines:
		try:
			instruction, value = lines[line]
		except KeyError:
			break
		if instruction == 'acc':
			acc += value
			used_lines.append(line)
			line += 1
			continue
		elif instruction == 'nop':
			used_lines.append(line)
			line += 1
			continue
		elif instruction == 'jmp':
			used_lines.append(line)
			line_jump = value
			line += line_jump
			continue
	return acc, used_lines


def parse_lines(lines):
	# parse the lines into a dict of line number and instructions, then we can use
	# the dict in a loop to reverse every nop/jmp
	line_instructions = {}
	nop_jmp_lines = []
	for index, line in enumerate(lines):
		instruction, number = line.split()
		line_instructions[index] = [instruction, int(number)]
		if instruction in ('jmp', 'nop'):
			nop_jmp_lines.append(index)
	return nop_jmp_lines, line_instructions


def part_2(swap_lines, instructions):
	record = {}
	zeroes = []
	for swap in swap_lines:
		swapped_instructions = instructions
		if swapped_instructions[swap][0] == 'jmp':
			swapped_instructions[swap][0] = 'nop'
		else:
			swapped_instructions[swap][0] = 'jmp'
		value, used_lines = part_1(swapped_instructions)
		record[swap] = value
		if len(instructions.keys()) - 1 in used_lines:
			zeroes.append(swap)
	return value, swap


swap_lines, instructions = parse_lines(inp)
answerp1, used = part_1(instructions)
print(answerp1)
# try re-parsing the input into a dict with line numbers as keys

# then brute force the solution by running accumulator for each changed instruction set
print(part_2(swap_lines, instructions))
