def main(a, b, c, d, lines, i=0):
    registers = {'a': a,
                 'b': b,
                 'c': c,
                 'd': d}

    while i < len(lines):
        print(i, registers, lines[i])
        parts = lines[i].split()
        instruction = parts[0]
        register = parts[1]
        if instruction == 'cpy':
            copy_register = parts[2]
            if register.isnumeric():
                registers[copy_register] = int(register)
            else:
                registers[copy_register] = registers[register]
        elif instruction == 'inc':
            registers[register] += 1
        elif instruction == 'jnz':
            if register.isnumeric() and int(register) != 0:
                i += int(parts[2])
                continue
            value = registers[register]
            if registers[register] != 0:
                i += int(parts[2])
                continue
        elif instruction == 'dec':
            registers[register] -= 1
        i += 1
    return registers


if __name__ == '__main__':
    with open('./input/day12.txt') as f:
        lines = f.readlines()
    # takes a very long time
    print(main(0, 0, 0, 0, lines))
    print(main(0, 0, 1, 0, lines))
