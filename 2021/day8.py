digit_lengths = {1: 2,
				 4: 4,
				 7: 3,
				 8: 7,
				 }


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


def solve_fives_and_sixes(wires, four, number_dict):
	fives = wires[3:6]
	sixes = wires[6:9]
	for five in fives:
		if number_dict['1'].issubset(set(five)):
			number_dict['3'] = set(five)
		elif four.issubset(set(five)):
			number_dict['5'] = set(five)
		else:
			number_dict['2'] = set(five)
	for six in sixes:
		if number_dict['4'].issubset(set(six)):
			number_dict['9'] = set(six)
		elif four.issubset(set(six)):
			number_dict['6'] = set(six)
		else:
			number_dict['0'] = set(six)
	return number_dict


def get_value(number_dict, strings):
	value = ''
	for s in strings:
		for k, v in number_dict.items():
			if set(s) == v:
				value += k
	return int(value)


def part2(lines):
	sum_of_output_values = 0
	numbers = {}
	for line in lines:
		signal_pattern_str, output_str = line.strip().split(' | ')
		outputs = output_str.strip().split()
		wires = sorted(signal_pattern_str.split(), key=len)
		numbers['7'] = set(wires[1])
		numbers['8'] = set(wires[-1])
		numbers['4'] = set(wires[2])
		numbers['1'] = set(wires[0])
		fourdiff = numbers['4'].difference(numbers['1'])
		five_six_dict = solve_fives_and_sixes(wires, fourdiff, numbers)
		numbers.update(five_six_dict)
		output_value = get_value(numbers, outputs)
		sum_of_output_values += output_value

		# https://www.reddit.com/r/adventofcode/comments/rbvpui/2021_day_8_part_2_my_logic_on_paper_i_used_python/

	return sum_of_output_values


if __name__ == '__main__':
	FILENAME = './input/day8.txt'
	with open(FILENAME) as f:
		lines = f.readlines()

	print(part1(lines))
	print(part2(lines))