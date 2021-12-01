def part1(depths):
	increase_count = 0
	for i, v in enumerate(depths):
		if i == 0:
			continue
		if depths[i] > depths[i-1]:
			increase_count += 1
	return increase_count


def part2(depths):
	window_sum_increases = 0  # counter
	# initialize sum of first three-measurement window
	current_window_sum = sum(depths[:3])

	# check each three-measurement window up until the third last index
	for i in range(1, len(depths) - 2):
		next_window_sum = sum(depths[i:(i + 3)])
		if next_window_sum > current_window_sum:
			window_sum_increases += 1
		current_window_sum = next_window_sum

	return window_sum_increases


if __name__ == '__main__':
	with open('./input/day1.txt') as f:
		depths = [int(x) for x in f.read().split('\n')]

	print(part1(depths))
	print(part2(depths))
