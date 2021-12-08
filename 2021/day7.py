from math import inf

def calc_fuel_constant_rate(crabs, align_position):
	fuel = 0
	for crab in crabs:
		fuel += abs(align_position - crab)
	return fuel


def calc_fuel_linear_rate(crabs, align_position):
	fuel = 0
	for crab in crabs:
		steps = abs(align_position - crab)
		fuel += (steps + 1) * steps / 2  # sum of increasing series formula
	return int(fuel)


def align_crabs(crabs, fuel_rate):
	# crabs can align at any position
	max_position = max(crabs)
	min_fuel = inf
	# check all possible positions
	for position in range(max_position):
		fuel_required = calc_fuel_constant_rate(crabs, position) if fuel_rate == 'constant' else \
			calc_fuel_linear_rate(crabs, position)
		if fuel_required < min_fuel:
			min_fuel = fuel_required
	return min_fuel


if __name__ == '__main__':
	FILENAME = './input/day7.txt'
	with open(FILENAME) as f:
		crab_positions = list(map(int, f.read().strip().split(',')))

	#crab_positions = [16,1,2,0,4,2,7,1,2,14]
	print(align_crabs(crab_positions, 'constant'))
	print(align_crabs(crab_positions, 'linear'))


