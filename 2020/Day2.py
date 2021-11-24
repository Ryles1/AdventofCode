#! python3

with open('input.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    temp = line.split(':')
    passwd = temp[1].strip()
    letter = temp[0][-1]
    nums = temp[0].split()[0].split('-')
    min = int(nums[0])
    max = int(nums[1])
    if min <= passwd.count(letter) <= max:
        count += 1

print(count)
