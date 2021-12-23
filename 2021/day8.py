digit_lengths = {1: 2,
				 4: 4,
				 7: 3,
				 8: 7,
				 0: 6,
				 9: 6,
				 6: 6,
				 5: 5,
				 2: 5,
				 3: 5}


def count_1478(outputs):
	count = 0
	for o in outputs:
		count += 1 if len(o) in digit_lengths.values() else 0
	return count


def part1(lines):
	count_of_1478 = 0
	for line in lines:
		signal_pattern_str, output_str = line.strip().split(' | ')
		outputs = output_str.strip().split()
		count_of_1478 += count_1478(outputs)
	return count_of_1478


def get_blank_dict():
	w = {'top': None, 'mid': None, 'bottom': None, 'topleft': None, 'topright': None,
		 'botleft': None, 'botright': None}
	return w


def part2(lines):
	sum_of_output_values = 0
	connections = get_blank_dict()
	numbers = {}
	for line in lines:
		signal_pattern_str, output_str = line.strip().split(' | ')
		outputs = output_str.strip().split()
		wires = sorted(signal_pattern_str.split(), key=len)
		numbers['seven'] = set(wires[1])
		numbers['eight'] = set(wires[-1])
		numbers['four'] = set(wires[2])
		numbers['one'] = set(wires[0])
		fourdiff = four.difference(one)

		# https://www.reddit.com/r/adventofcode/comments/rbvpui/2021_day_8_part_2_my_logic_on_paper_i_used_python/

		# use the difference in the digit arrangements and maybe sets to determine
		# the wire outputs  eg. 7 only has one more segment than 1 so top is easy to determine
		pass
	return


if __name__ == '__main__':
	FILENAME = './input/day8.txt'
	with open(FILENAME) as f:
		lines = f.readlines()

	print(part1(lines))
	print(part2(lines))