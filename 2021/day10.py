from statistics import median
matches = ['()', '{}', '[]', '<>']
openers = ['(', '{', '[', '<']
closers = [')', '}', ']', '>']


def check_line(line):
	stack = []
	for i, c in enumerate(line):
		if c in openers:
			stack.append(c)
		else:
			opener = stack.pop()
			pair = f'{opener}{c}'
			if pair not in matches:
				expected = closers[openers.index(opener)]
				return c
	return ''


def calculate_score(counts):
	score_points = {')': 3,
			  ']': 57,
			  '}': 1197,
			  '>': 25137}

	s = list(score_points.values())
	c = list(counts.values())
	score = sum([x * y for x, y in zip(s, c)])
	return score


def part1(lines):
	incomplete = []
	illegal_counter = {')': 0,
		  ']': 0,
		  '}': 0,
		  '>': 0}
	for i, line in enumerate(lines):
		illegal_char = check_line(line)
		if illegal_char in illegal_counter:
			illegal_counter[illegal_char] += 1
		else:
			incomplete.append(line)
	score = calculate_score(illegal_counter)
	return score, incomplete


def update_score(str):
	score = 0
	score_points = {')': 1,
					']': 2,
					'}': 3,
					'>': 4}
	for c in str:
		score *= 5
		score += score_points[c]
	return score


def complete_line(incomplete):
	stack = []
	for i, c in enumerate(incomplete):
		if c in openers:
			stack.append(c)
		else:
			opener = stack.pop()
			pair = f'{opener}{c}'
			if pair not in matches:
				break
	reversed_stack = reversed(stack)
	# create the completion string from inside to outside
	completion = [closers[openers.index(c)] for c in reversed_stack]
	completion = ''.join(completion)
	return completion


def part2(lines):
	scores = []
	for line in lines:
		completion_string = complete_line(line)
		score_increment = update_score(completion_string)
		scores.append(score_increment)
	middle_score = median(sorted(scores))
	return middle_score


if __name__ == '__main__':
	FILENAME = './input/day10.txt'
	with open(FILENAME) as f:
		lines = f.readlines()
		lines = [line.strip() for line in lines]

	part1_score, incomplete_lines = part1(lines)
	print(part1_score)

	print(part2(incomplete_lines))
