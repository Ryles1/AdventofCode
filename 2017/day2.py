import itertools

nums = [list(map(lambda x: int(x), line.split())) for line in open('./input/day2.txt').read().strip().split('\n')]

checksum = sum([max(line) - min(line) for line in nums])

print(checksum)

nums_sorted = sorted(nums)

checksum2 = 0

for line in nums_sorted:
    combs = itertools.permutations(line,2)
    for comb in combs:
        if comb[0] % comb[1] == 0:
            checksum2 += comb[0] // comb[1]
            break

print(checksum2)