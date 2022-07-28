def count_code_characters(s):
    length = 0
    i = 0
    s = s.strip().strip('"')
    while i < len(s):
        window = s[i: i + 2]
        if window == r'\"':
            length += 1
            i += 2
        elif window == r'\x':
            length += 1
            i += 4
        elif window == r'\\':
            length += 1
            i += 2
        else:
            length += 1
            i += 1
    return length


def part1(lines):
    code_total_length = 0
    string_total_length = 0
    for line in lines:
        code_total_length += len(line.strip())
        string_total_length += count_code_characters(line)
    answer = code_total_length - string_total_length
    return answer


def count_encoded_characters(s):
    length = 2  # account for starting and ending "
    i = 0
    s = s.strip()
    while i < len(s):
        if s[i] == '"':
            length += 2  # add \ before every "
            i += 1
        elif s[i] == '\\':
            length += 2  # add \ before every \
            i += 1
        else:
            length += 1
            i += 1
    return length


def part2(lines):
    code_total_length = 0
    encoded_total_characters = 0
    for line in lines:
        code_total_length += len(line.strip())
        encoded_total_characters += count_encoded_characters(line)
    answer = encoded_total_characters - code_total_length
    return answer

if __name__ == '__main__':
    with open('./input/day8.txt') as f:
        santas_list = f.readlines()

    print(part1(santas_list))
    print(part2(santas_list))
