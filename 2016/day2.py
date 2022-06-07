moves_part1 = {1: {'D': 4, 'R': 2},
               2: {'L': 1, 'R': 3, 'D': 5},
               3: {'L': 2, 'D': 6},
               4: {'D': 7, 'R': 5, 'U': 1},
               5: {'L': 4, 'R': 6, 'D': 8, 'U': 2},
               6: {'L': 2, 'D': 9, 'U': 3},
               7: {'U': 4, 'R': 8},
               8: {'L': 7, 'R': 9, 'U': 5},
               9: {'L': 8, 'U': 6},
               }

moves_part2 = {1: {'D': 3},
               2: {'D': 6, 'R': 3},
               3: {'D': 7, 'R': 4, 'U': 1, 'L': 2},
               4: {'D': 8, 'L': 3},
               5: {'R': 6},
               6: {'D': 'A', 'R': 7, 'U': 2, 'L': 5},
               7: {'D': 'B', 'R': 8, 'U': 3, 'L': 6},
               8: {'D': 'C', 'U': 4, 'L': 7, 'R': 9},
               9: {'L': 8},
               'A': {'R': 'B', 'U': 6},
               'B': {'D': 'D', 'R': 'C', 'U': 7, 'L': 'A'},
               'C': {'L': 'B', 'U': 8},
               'D': {'U': 'B'},
               }


def get_button(instructions, start, part2=False):
    current = start
    next = current
    moves = moves_part2 if part2 else moves_part1
    for i, letter in enumerate(instructions):
        next = moves.get(current).get(letter, next)
        current = next
    return next


def main(lines, part2=False):
    start = 5
    code = []
    for line in lines:
        code.append(get_button(line, start, part2))
        start = code[-1]
    code = ''.join([str(i) for i in code])
    return code


if __name__ == '__main__':
    with open('./input/day2.txt') as f:
        instructions = f.read().strip().split('\n')
    instructions = [line.strip() for line in instructions]
    print(main(instructions))
    print(main(instructions, True))
