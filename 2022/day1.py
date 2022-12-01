def parse(s):
    groups = s.split('\n\n')
    elves = []
    for group in groups:
        elf = tuple([int(f.strip()) for f in group.split('\n')])
        elves.append(elf)
    return elves


if __name__ == '__main__':
    with open('./input/day1.txt') as f:
        raw = f.read().strip()

    elves = parse(raw)

    sorted_elves = sorted(elves, key=sum, reverse=True)
    print(sum(sorted_elves[0]))

    print(sum([sum(elf) for elf in sorted_elves[:3]]))
