import re


def main1(lines):
    calibration_sum = 0
    for line in lines:
        digits = re.findall(r'\d', line)
        calibration = digits[0] + digits[-1]
        calibration_sum += int(calibration)
    return calibration_sum


def main2(lines):
    calibration_sum = 0
    digit_words = {'one': 1, 'two': 2,'three': 3, 'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,
                   'eno': 1,'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9}
    for line in lines:
        digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        first_digit: str = digits[0]
        first_digit = first_digit if first_digit.isdigit() else str(digit_words[first_digit])
        digits_reverse = re.findall(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', ''.join(list(reversed(line))))
        second_digit = digits_reverse[0]
        second_digit = second_digit if second_digit.isdigit() else str(digit_words[second_digit])
        calibration = first_digit + second_digit
        calibration_sum += int(calibration)
    return calibration_sum


if __name__ == '__main__':
    with open('./input/day1.txt') as f:
        lines = f.read().strip().split('\n')

    answer1 = main1(lines)
    print(answer1)

    answer2 = main2(lines)
    print(answer2)
