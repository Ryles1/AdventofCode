def decompress1(file_str):
    index = 0
    decompressed_length = 0
    decompressed_list = []
    while index < len(file_str):
        next_char = file_str[index]
        if next_char != '(':
            decompressed_length += 1
            index += 1
        else:
            # find the next ')' - assuming the next ")" is within the next 10 characters
            close_bracket_index = file_str.index(')', index, index + 10)
            # marker_str is the (AxB) that indicates the number of characters and num of repeats
            marker_str = ''.join(file_str[index + 1: close_bracket_index])
            num_chars, num_repeats = (int(num) for num in marker_str.split('x'))
            next_repeat_str = file_str[close_bracket_index + 1: (close_bracket_index + 1 + num_chars)]
            decompressed_length += len((next_repeat_str * num_repeats))
            index = close_bracket_index + 1 + num_chars
    return decompressed_length


def decompress2(file_str):
    index = 0
    decompressed_length = 0
    while index <= len(file_str):
        # recursive base case
        if index == len(file_str):
            return decompressed_length

        next_char = file_str[index]
        if next_char != '(':
            decompressed_length += 1
            index += 1
        else:
            # find the next ')' - assuming the next ")" is within the next 10 characters
            close_bracket_index = file_str.index(')', index, index + 10)
            # marker_str is the (AxB) that indicates the number of characters and num of repeats
            marker_str = ''.join(file_str[index + 1: close_bracket_index])
            num_chars, num_repeats = (int(num) for num in marker_str.split('x'))
            # get the remaining string and send it to be decompressed
            next_repeat_str = file_str[close_bracket_index + 1: (close_bracket_index + 1 + num_chars)]
            new_length = decompress2(next_repeat_str)
            decompressed_length += (new_length * num_repeats)
            index = close_bracket_index + 1 + num_chars
    return decompressed_length


if __name__ == '__main__':
    with open('./input/day9.txt') as f:
        data = f.read().strip()

    data_no_spaces = [c for c in data if c != ' ']
    print(decompress1(data_no_spaces))
    print(decompress2(data_no_spaces))
