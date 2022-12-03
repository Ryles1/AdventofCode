letters = 'abcdefghijklmnopqrstuvwxyz'
priorities = dict(zip(letters, range(1, 27)))


def part1(lines):
    common_items_and_priorities = []
    for line in lines:
        items = line.strip()
        comp1, comp2 = items[:len(items)//2], items[len(items)//2:]
        set1 = set(comp1)
        set2 = set(comp2)
        common_item = set1.intersection(set2)
        common_item = common_item.pop()
        priority = priorities[common_item.lower()]
        priority += 26 if common_item.isupper() else 0
        common_items_and_priorities.append((common_item, priority))
    return sum([item[1] for item in common_items_and_priorities])


def part2(lines):
    badge_priorities = []
    for i in range(0, len(lines), 3):
        sack1, sack2, sack3 = lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()
        set1, set2, set3 = set(sack1), set(sack2), set(sack3)
        common_item = set1.intersection(set2, set3)
        common_item = common_item.pop()
        priority = priorities[common_item.lower()]
        priority += 26 if common_item.isupper() else 0
        badge_priorities.append(priority)
    return sum(badge_priorities)


if __name__ == '__main__':
    with open('./input/day3.txt') as f:
        lines = f.readlines()

    print(part1(lines))
    print(part2(lines))
