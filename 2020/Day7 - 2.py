#! python3

with open('input.txt') as f:
    lines = f.read().strip().split('\n')

bag_tree = {}

for i, line in enumerate(lines):
    print(i)
    bag = line.split(' contain ')[0][:-5]
    bag_tree[bag] = []
    for contained_bag in line.split(' contain ')[1].split(', '):
        if contained_bag.startswith('no'):
            continue
        num = int(contained_bag.strip()[0])
        if 'bags' in contained_bag:
            bag_tree[bag].append((contained_bag[2:-5],num))
        else:
            bag_tree[bag].append((contained_bag[2:-4], num))

print(bag_tree.items())