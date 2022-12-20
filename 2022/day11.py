def get_items(monkeys):
    items = []
    for s in monkeys:
        lines = [l.strip() for l in s.split('\n')]
        items.append([int(i.strip()) for i in lines[1].split(':')[1].split(',')])
    return items


def get_throws(monkeys):
    throws = {}
    for i, s in enumerate(monkeys):
        lines = [l.strip() for l in s.split('\n')]
        throws[i] = {}
        throws[i]['true'] = int(lines[4].split()[-1])
        throws[i]['false'] = int(lines[5].split()[-1])
    return throws


def main(monkeys, num_rounds, worry_func):
    items = get_items(monkeys)
    operations = [lambda x: x * 13,
                  lambda x: x + 3,
                  lambda x: x + 6,
                  lambda x: x + 2,
                  lambda x: x * x,
                  lambda x: x + 4,
                  lambda x: x * 7,
                  lambda x: x + 7,
                  ]
    tests = [lambda x: x % 19,
             lambda x: x % 2,
             lambda x: x % 13,
             lambda x: x % 5,
             lambda x: x % 7,
             lambda x: x % 11,
             lambda x: x % 17,
             lambda x: x % 3,
             ]
    throw_to = get_throws(monkeys)
    inspection_counts = [0 for _ in range(len(items))]

    for round in range(num_rounds):
        if round % 100 == 0:
            print(round)
        for monkey in throw_to.keys():
            while len(items[monkey]) > 0:
                worry_level = items[monkey][0]
                # inspect item
                items[monkey][0] = operations[monkey](worry_level)
                # update count
                inspection_counts[monkey] += 1
                # adjust worry level
                items[monkey][0] = worry_func(items[monkey][0])
                # test worry level
                test_answer = tests[monkey](items[monkey][0])
                # get item in a temp variable
                temp = items[monkey][0]
                # redefine monkey item list to exclude first item
                items[monkey] = items[monkey][1:]
                if test_answer == 0:
                    throw_to_monkey = throw_to[monkey]['true']
                else:
                    throw_to_monkey = throw_to[monkey]['false']
                items[throw_to_monkey].append(temp)
    inspection_counts.sort(reverse=True)
    monkey_business = inspection_counts[0] * inspection_counts[1]
    return monkey_business


if __name__ == '__main__':
    with open('./input/day11.txt') as f:
        monkeys = f.read().strip().split('\n\n')

    part1_worry_func = lambda x: x // 3
    print(main(monkeys, 20, part1_worry_func))
