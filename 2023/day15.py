def HASH_algo(s):
    current_value = 0
    ascii_codes = list(map(ord, s))
    for code in ascii_codes:
        current_value += code
        current_value *= 17
        current_value %= 256
    return current_value


def main1(strings):
    hash_values = []
    answer1 = 0
    for string in strings:
        hash_values.append(HASH_algo(string))
    answer1 = sum(hash_values)
    return answer1


def isLabelPresent(label, lenses):
    for lense in lenses:
        if lense[0] == label:
            return True
    return False


def getIndex(label, lenses):
    for i, lense in enumerate(lenses):
        if label == lense[0]:
            return i
    return None


def main2(strings):
    boxes = {k: [] for k in range(256)}
    focusing_power = 0
    for string in strings:
        label = string[:-1] if '-' in string else string[:-2]
        focal_length = int(string[-1]) if '=' in string else 0
        box_num = HASH_algo(label)
        operation = '-' if '-' in string else '='
        lens = (label, focal_length)
        if operation == '-':
            lens_index = getIndex(label, boxes[box_num])
            if lens_index is None:
                continue
            else:
                del boxes[box_num][lens_index]
        if operation == '=':
            if len(boxes[box_num]) == 0 or not isLabelPresent(label, boxes[box_num]):
                boxes[box_num].append(lens)
            else:
                lens_index = getIndex(label, boxes[box_num])
                boxes[box_num][lens_index] = lens
    for box_num, box in enumerate(boxes.values()):
        power = sum([(box_num + 1) * (i + 1) * box[i][1] for i in range(len(box))])
        focusing_power += power
    return focusing_power


if __name__ == '__main__':
    with open('./input/day15.txt') as f:
        line = f.read().strip()
    strings = line.split(',')

    answer1 = main1(strings)
    print(answer1)
    answer2 = main2(strings)
    print(answer2)
