#! python3

with open('input-Day8.txt') as f:
    inp = f.read().split('\n')

def part_1(lines):
    acc = 0
    used_lines = []
    line = 0
    while line not in used_lines:
        instruction = lines[line].split()

        if instruction[0] == 'acc':
            acc += int(instruction[1])
            used_lines.append(line)
            line += 1
            continue
        elif instruction[0] == 'nop':
            used_lines.append(line)
            line += 1
            continue
        elif instruction[0] == 'jmp':
            used_lines.append(line)
            line_jump = int(instruction[1])
            line += line_jump
            continue
    return acc, used_lines[-20:]


def check_line(check, used):
    if check in used:
        return True

def part_2(lines):
    acc = 0
    used_lines = []
    line = 0
    change_line = None
    instruction = True
    while instruction:
        instruction = lines[line].split()
        command = instruction[0] if instruction else None
        #print(line)
        if command == 'acc':
            acc += int(instruction[1])
            used_lines.append(line)
            line += 1
            continue
        elif command == 'nop':
            if check_line(line + 1, used_lines) and change_line is None:
                print(f'Changing line {line} from {command} to jmp')
                command = 'jmp'
                change_line = line
                used_lines.append(line)
                line += 1
                continue
            else:
                used_lines.append(line)
                line += 1
                continue
        elif command == 'jmp':
            line_jump = int(instruction[1])
            if check_line((line + line_jump), used_lines) and change_line is None:
                print(f'Changing line {line} from {command} to nop')
                command = 'nop'
                change_line = line
                used_lines.append(line)
                line += 1
                continue
            else:
                used_lines.append(line)
                line += line_jump
                continue
        
    return acc, change_line


#map = {}
#for i, line in enumerate(lines):
 #   next_line = line.split()
    #map[i] =

print(part_1(inp))
print(part_2(inp))