def get_lines(data):
    return data.split('\n')


def main(data):
    lines = get_lines(data)
    position_char_counts = get_position_char_counts(lines)

    p1_message_chars = []
    for position, counts in position_char_counts.items():
        p1_message_chars.append(most_common_char_for_position(counts))

    p1_message = ''.join(p1_message_chars)

    p2_message_chars = []
    for position, counts in position_char_counts.items():
        p2_message_chars.append(least_common_char_for_position(counts))

    p2_message = ''.join(p2_message_chars)

    return p1_message, p2_message


def get_position_char_counts(lines):
    position_count = {i: {} for i in range(len(lines[0]))}
    for line in lines:
        for i, char in enumerate(line):
            try:
                position_count[i][char] += 1
            except KeyError:
                position_count[i][char] = 1
    return position_count


def least_common_char_for_position(counts):
    least_common = None
    smallest_count = 0
    for char, count in counts.items():
        if least_common is None:
            least_common = char
            smallest_count = count
        else:
            if count < smallest_count:
                least_common = char
                smallest_count = count
    return least_common


def most_common_char_for_position(counts):
    most_common = None
    largest_count = 0
    for char, count in counts.items():
        if most_common is None:
            most_common = char
            largest_count = count
        else:
            if count > largest_count:
                most_common = char
                largest_count = count
    return most_common


if __name__ == '__main__':
    with open('./input/day6.txt') as f:
        data = f.read().strip()

    print(main(data))
