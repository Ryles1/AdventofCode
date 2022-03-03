from itertools import product


def get_numbers(data):
	possible_zdiv1_combs = list(product([9, 8, 7, 6, 5, 4, 3, 2, 1], repeat=7))
	valid = []
	for comb in possible_zdiv1_combs:
		num = calculate(data, comb)

		if num != 0:
			valid.append(num)

	return valid


def calculate(data, comb):
	z = 0
	number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	ws = iter([str(_) for _ in comb])
	for i in range(14):
		if data[i]['z_div'] == 1:
			w = int(next(ws))
			number[i] = w
			z = z * 26 + w + data[i]['y_const']

		if data[i]['z_div'] == 26:
			x1 = z % 26 + data[i]['x_const']
			if not 1 <= x1 <= 9:
				return 0
			else:
				number[i] = x1
				z = z // 26
	final_number = int(''.join([str(_) for _ in number]))
	if z == 0:
		return final_number
	else:
		return 0


def parse_instructions(lines):
	vars = []
	important_lines = [4, 5, 15]
	for i in range(14):
		temp_vars = {'w': 0, 'z_div': 0, 'x1': 0, 'x_const': 0, 'y_const': 0, 'z': 0}
		for j in important_lines:
			line = i * 18 + j
			if j == 4:
				temp_vars['z_div'] = int(lines[line].split()[-1])
			if j == 5:
				temp_vars['x_const'] = int(lines[line].split()[-1])
			if j == 15:
				temp_vars['y_const'] = int(lines[line].split()[-1])
		vars.append(temp_vars)
	return vars


if __name__ == '__main__':
	with open('./input/day24.txt') as f:
		lines = f.readlines()

	data = parse_instructions(lines)
	numbers = get_numbers(data)
	print(max(numbers))
	print(min(numbers))
