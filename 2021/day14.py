from collections import Counter


def parse_instructions(raw_instructions):
	instructions_dict = {}
	for i, v in enumerate(raw_instructions):
		pair, insertion = v.split(' -> ')
		instructions_dict[pair] = insertion
	return instructions_dict


def get_final_answer(count):
	count_values = list(sorted(count.values()))
	most_common = count_values[-1]
	least_common = count_values[0]
	return most_common - least_common


def populate_pairs(polymer, initial_pairs):
	for i in range(len(polymer) - 1):
		pair = polymer[i: i + 2]
		initial_pairs[pair] += 1
	return initial_pairs


def polymer_insertion(template, raw_rules, steps):
	rules = parse_instructions(raw_rules)
	pairs = {key: 0 for key in rules.keys()}
	pairs = populate_pairs(template, pairs)
	counter = Counter(template)
	for step in range(steps):
		pairs_to_check = {key: value for key, value in pairs.items() if value > 0}
		for key in pairs_to_check.keys():
			key_count = pairs_to_check[key]
			new_char = rules[key]
			new_pair1 = key[0] + new_char
			new_pair2 = new_char + key[1]
			pairs[key] -= key_count
			pairs[new_pair1] += key_count
			pairs[new_pair2] += key_count
			counter[new_char] += key_count

	answer = get_final_answer(counter)
	return answer


if __name__ == '__main__':
	FILENAME = './input/day14.txt'
	with open(FILENAME) as f:
		s = f.read()
		L = s.split('\n')
		template, rule_lines = L[0], L[2:]

	print(polymer_insertion(template, rule_lines, 10))
	print(polymer_insertion(template, rule_lines, 40))
