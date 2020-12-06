#! python3

with open('input.txt') as f:
    lines = f.read().strip()

groups = lines.split('\n\n')

part1_num = sum([len(set(group.replace('\n', ''))) for group in groups])

print(part1_num)

group2 = lines.split('\n\n')

nums = []
for group in group2:
    temp = group.split('\n')
    num = len(set.intersection(*[set(t) for t in temp]))
    nums.append(num)

print(sum(nums))

