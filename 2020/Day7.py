#! python3

with open('input.txt') as f:
    lines = f.read().strip().split('\n')

bags = set()
holds_gold = set()
for line in lines:
    contained_bags, container_bag = line.split('contain')[1], line.split('contain')[0]
    bags.add(container_bag)
    if 'shiny gold' in contained_bags:
        holds_gold.add(container_bag[:-5])

new_bags = set([1])
for _ in range(1000):
    new_bags = set()
    for line in lines:
        temp = None
        contained_bags, container_bag = line.split('contain')[1], line.split('contain')[0]
        for bag in holds_gold:
            if bag in contained_bags:
                temp = container_bag
        if temp:
            new_bags.add(temp)
    holds_gold.update(new_bags)

print(len(holds_gold))