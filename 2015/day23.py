def main(a, b, lines):
    i = 0
    while i < len(lines):
        #print(i, a, b, lines[i])
        parts = lines[i].split()
        if parts[0] == 'hlf':
            a //= 2 if parts[1] == 'a' else 1
            b //= 2 if parts[1] == 'b' else 1
        elif parts[0] == 'tpl':
            a *= 3 if parts[1] == 'a' else 1
            b *= 3 if parts[1] == 'b' else 1
        elif parts[0] == 'inc':
            a += 1 if parts[1] == 'a' else 0
            b += 1 if parts[1] == 'b' else 0
        elif parts[0] == 'jmp':
            i += int(parts[1])
            continue
        elif parts[0] == 'jie':
            register = parts[1][0]
            offset = int(parts[2])
            if register == 'a' and a % 2 == 0:
                i += offset
                continue
            if register == 'b' and b % 2 == 0:
                i += offset
                continue
        elif parts[0] == 'jio':
            register = parts[1][0]
            offset = int(parts[2])
            if register == 'a' and a == 1:
                i += offset
                continue
            if register == 'b' and b == 1:
                i += offset
                continue
        i += 1
    return a, b


if __name__ == '__main__':
    with open('./input/day23.txt') as f:
        lines = f.readlines()

    print(main(0, 0, lines))
    print(main(1, 0, lines))
