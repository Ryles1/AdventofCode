import re
PATTERN1 = re.compile(r'mul\((\d+),(\d+)\)')
PATTERN2 = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")


def main1(inp):
    instructions = re.findall(PATTERN1, inp)
    total = 0
    for line in instructions:
        total += int(line[0]) * int(line[1])
    return total


def main2(inp):
    instructions = re.findall(PATTERN2, inp)
    enabled = True
    total = 0
    for line in instructions:
        if "don't()" in line:
            enabled = False
            continue
        elif "do()" in line:
            enabled = True
            continue
        elif enabled is True:
            total += int(line[0]) * int(line[1])
    return total


if __name__ == '__main__':
    with open('./input/day3.txt') as f:
        inp = f.read().strip()

    answer1 = main1(inp)
    print(answer1)

    answer2 = main2(inp)
    print(answer2)
