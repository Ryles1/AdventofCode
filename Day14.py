#! python3
import itertools

def apply_mask1(mask, string):
    updated = []
    for i, v in enumerate(string):
        if mask[i] == 'X':
            updated.append(v)
        else:
            updated.append(mask[i])
    return int(''.join(updated),2)


def part1(lines):
    memory = {}
    mask = ''
    for line in lines:
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
        else:
            address = line.split('=')[0].strip()[4:-1]
            start_value = line.split('=')[1].strip()
            start_value = f'{int(start_value):036b}'
            final_value = apply_mask1(mask, start_value)
            memory[address] = final_value
    return memory


def apply_mask2(mask, add):
    adds = []
    xcount = mask.count('X')
    bitgen = itertools.product('01', repeat=xcount)
    for bg in bitgen:
        new_add = []
        gen = (g for g in bg)
        for i, v in enumerate(add):
            if mask[i] == '0':
                new_add.append(v)
            elif mask[i] == '1':
                new_add.append('1')
            elif mask[i] == 'X':
                new_add.append(next(gen))
        adds.append(int(''.join(new_add), 2))
    return adds


def part2(lines):
    memory = {}
    mask = ''
    for line in lines:
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
        else:
            address = line.split('=')[0].strip()[4:-1]
            address = f'{int(address):036b}'
            value = int(line.split('=')[1].strip())
            addresses = apply_mask2(mask, address)
            for a in addresses:
                memory[a] = value
    return memory


if __name__ == '__main__':
    with open('input-Day14.txt') as f:
        lines = f.readlines()

    answer1 = part1(lines)
    print(sum(answer1.values()))
    answer2 = part2(lines)
    print(sum(answer2.values()))