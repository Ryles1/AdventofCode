from math import prod


def convert_hex_to_bin(message):
	bin_list = []
	for h in message:
		bits = f'{int(h, 16):b}'.zfill(4)
		bin_list.append(bits)
	return ''.join(bin_list)


def greater(iterable):
	return 1 if iterable[0] > iterable[1] else 0


def less(iterable):
	return 1 if iterable[0] < iterable[1] else 0


def equal(iterable):
	return 1 if iterable[0] == iterable[1] else 0


def decode_bits(message_in_binary, length=0):
	if set(message_in_binary) == {'0'}:
		return [], []

	version_numbers = []
	# get the first three bits in the bit string and convert to base 10 integer
	version_str = message_in_binary[:3]
	version = int(version_str, 2)
	version_numbers.append(int(version))
	# the type id is the second group of 3 bits
	type_id_str = message_in_binary[3:6]
	type_id = int(type_id_str, 2)

	length += 6

	#  packet type id (4 = literal, anything else = operator)
	isLiteral = True if type_id == 4 else False
	literal = ''
	packets = []
	if isLiteral:

		print('Literal')

		packet = version_str + type_id_str
		# for a literal, every group of five bits after is a piece of the number
		# get groups of five bits until the first bit in the group is a 0
		# and add the four bits to the literal value
		i = 6
		while True:
			next_group = message_in_binary[i: i + 5]
			packet += next_group
			prefix = next_group[0]
			group = next_group[1:]
			literal += group
			i += 5
			if prefix == '0':
				break
		packets.append(packet)
		literal_values = [int(literal,2)]
		return packets, version_numbers, literal_values
	else:
		# for an operator, the 7th bit is the length type ID
		length_id = message_in_binary[6]
		length += 1
		literal_values = []
		if length_id == '0':
			print('Operator type 0')
			# 0 - next 15 bits are a number for the total length (in bits) of subpackets contained by this packet
			length_of_sub_packets_binary = message_in_binary[7:22]
			length += 15
			length_of_sub_packets = int(length_of_sub_packets_binary, 2)
			new_packets = []
			sub_length = 0

			packets = [message_in_binary[:22]]
			while sub_length < length_of_sub_packets:
				start = length + sub_length
				p, v, l = decode_bits(message_in_binary[start:])
				if len(p) == 0:
					break
				new_packets.extend(p)
				version_numbers.extend(v)
				if l is not None:
					literal_values.extend(l)
				sub_length = len(''.join(new_packets))
			length += sub_length
			packets.extend(new_packets)
		elif length_id == '1':
			print('Operator type 1')
			# next 11 bits are a number for the number of subpackets contained by this packet
			number_of_sub_packets_binary = message_in_binary[7:18]
			number_of_sub_packets = int(number_of_sub_packets_binary, 2)
			new_packets = []
			length += 11
			sub_length = 0
			packets = [message_in_binary[:18]]
			for _ in range(number_of_sub_packets):
				start = sub_length + length
				p, v, l = decode_bits(message_in_binary[start:])
				new_packets.extend(p)
				version_numbers.extend(v)
				sub_length = len(''.join(new_packets))
				if l is not None:
					literal_values.extend(l)
			packets.extend(new_packets)
			length += sub_length
		if type_id == 0:
			literal_values = [sum(literal_values)]
		elif type_id == 1:
			literal_values = [prod(literal_values)]
		elif type_id == 2:
			literal_values = [min(literal_values)]
		elif type_id == 3:
			literal_values = [max(literal_values)]
		elif type_id == 5:
			literal_values = [greater(literal_values)]
		elif type_id == 6:
			literal_values = [less(literal_values)]
		elif type_id == 7:
			literal_values = [equal(literal_values)]
		return packets, version_numbers, literal_values


if __name__ == '__main__':
	FILENAME = './input/day16.txt'
	with open(FILENAME) as f:
		s = f.read()

	# convert hex to bin
	#s = 'D8005AC2A8F0'  test line
	binary_str = convert_hex_to_bin(s)

	packets_list, versions, value = decode_bits(binary_str)
	print(value)
	version_total = sum(versions)
	print(version_total)

