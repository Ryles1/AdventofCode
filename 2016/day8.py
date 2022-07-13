import copy

ON = '#'
OFF = '.'


def parse_command(line):
    return line.split()[0]


def process_rect(rect, screen):
    new_screen = copy.deepcopy(screen)
    length_x, length_y = int(rect.split('x')[0]), int(rect.split('x')[1])
    for y in range(length_y):
        for x in range(length_x):
            new_screen[y][x] = ON
    return new_screen


def rotate_row(row, shift):
    new_row = row[-shift:]
    new_row.extend(row[:-shift])
    return new_row


def rotate_col(screen, col, shift):
    # transpose the column in question to a row
    transposed_col = [screen[y][col] for y in range(len(screen))]
    # rotate the transposed row, send to function as screen with one row only
    rotated_transposed_col = rotate_row(transposed_col, shift)
    new_screen = copy.deepcopy(screen)
    for row in range(len(screen)):
        new_screen[row][col] = rotated_transposed_col[row]
    return new_screen


def count_lit_pixels(screen):
    lit_pixels = 0
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if screen[y][x] == ON:
                lit_pixels += 1
    return lit_pixels


def main1(lines, cols, rows):
    screen = [[OFF for _ in range(cols)] for __ in range(rows)]
    new_screen = copy.deepcopy(screen)
    for line in lines:
        cmd = parse_command(line)
        if cmd == 'rect':
            turn_on_pixels = line.split()[1]
            new_screen = process_rect(turn_on_pixels, screen)
        elif cmd == 'rotate':
            if 'x' in line:
                col = int(line.split()[2].split('=')[1])
                shift = int(line.split()[-1])
                new_screen = rotate_col(screen, col, shift)
            else:
                row = int(line.split()[2].split('=')[1])
                shift = int(line.split()[-1])
                row_to_shift = screen[row]
                new_row = rotate_row(row_to_shift, shift)
                new_screen = copy.deepcopy(screen)
                new_screen[row] = new_row
        screen = copy.deepcopy(new_screen)
    num_lit_pixels = count_lit_pixels(screen)
    print('\n'.join(''.join(x) for x in screen))
    return num_lit_pixels


if __name__ == '__main__':
    COLS = 50
    ROWS = 6
    with open('./input/day8.txt') as f:
        data = f.read().strip().split('\n')

    print(main1(data, COLS, ROWS))
