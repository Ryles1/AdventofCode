#! python3

import itertools

with open('input.txt') as f:
    lines = f.readlines()

nums = []
for i in lines:
    nums.append(int(i.strip()))

combs = itertools.combinations(nums, 2)

answer = 0
for j in combs:
    if sum(j) == 2020:
        answer = j[0]*j[1]

print(answer)
                
