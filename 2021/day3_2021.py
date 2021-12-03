def part1(bytes_list):
	most_common_bits = []  # most common bit in each position
	least_common_bits = []  # least common bit in each position

	# count each position in each byte
	for i in range(len(bytes_list[0])):
		one_count = 0
		zero_count = 0
		for byte in bytes_list:
			one_count += 1 if byte[i] == '1' else 0
			zero_count += 1 if byte[i] == '0' else 0
		if int(one_count) > int(zero_count):
			most_common_bits.append('1')
			least_common_bits.append('0')
		else:
			most_common_bits.append('0')
			least_common_bits.append('1')
	# create the strings
	gamma_rate_str = ''.join(most_common_bits)
	epsilon_rate_str = ''.join(least_common_bits)
	# convert strings to integer from a base 2 string
	gamma_rate = int(gamma_rate_str, 2)
	epsilon_rate = int(epsilon_rate_str, 2)
	power_consumption = gamma_rate * epsilon_rate
	return power_consumption


def get_most_common(bytes_list, i):
	one_count, zero_count = 0, 0
	for byte in bytes_list:
		one_count += 1 if byte[i] == '1' else 0
		zero_count += 1 if byte[i] == '0' else 0
	# return most common value, return 1 in the case of a tie
	return '1' if one_count >= zero_count else '0'


def get_least_common(bytes_list, i):
	one_count, zero_count = 0, 0
	for byte in bytes_list:
		one_count += 1 if byte[i] == '1' else 0
		zero_count += 1 if byte[i] == '0' else 0
	# return least common value, return 0 in the case of a tie
	return '1' if one_count < zero_count else '0'


def get_O2_rating_base2(bytes_list):
	O2_bytes = bytes_list[::1]  # copy bytes list to avoid list pointer issues
	i = 0
	max_i = len(O2_bytes)
	while len(O2_bytes) > 1 and i <= max_i:
		most_common = get_most_common(O2_bytes, i)
		O2_bytes = list(filter(lambda x: x[i] == most_common, O2_bytes))
		i += 1
	O2_rating_base2 = O2_bytes[0]
	return O2_rating_base2


def get_CO2_rating_base2(bytes_list):
	C02_bytes = bytes_list[::1]  # copy bytes list to avoid list pointer issues
	i = 0
	max_i = len(C02_bytes)
	while len(C02_bytes) > 1 and i <= max_i:
		least_common = get_least_common(C02_bytes, i)
		C02_bytes = list(filter(lambda x: x[i] == least_common, C02_bytes))
		i += 1
	C02_rating_base2 = C02_bytes[0]
	return C02_rating_base2


def part2(bytes_list):
	O2_gen_base2 = get_O2_rating_base2(bytes_list)
	CO2_scrubber_base2 = get_CO2_rating_base2(bytes_list)
	O2_gen_rating = int(O2_gen_base2, 2)
	CO2_scrubber_rating = int(CO2_scrubber_base2, 2)
	life_support_rating = O2_gen_rating * CO2_scrubber_rating
	return life_support_rating


if __name__ == '__main__':
	with open('./input/day3.txt') as f:
		lines = f.read().split('\n')

	print(part1(lines))
	print(part2(lines))
