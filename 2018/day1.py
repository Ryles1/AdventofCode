if __name__ == '__main__':
    with open('./input/day1.txt') as f:
        lines = f.readlines()


answer1: int = sum([int(x) for x in lines])

print(answer1)

counter: int = 0
i = 0
frequencies = set()
new_frequency = counter
while new_frequency not in frequencies:
    frequencies.add(new_frequency)
    if i == len(lines):
        i = 0
    counter += int(lines[i])
    new_frequency = counter
    i += 1

answer2 = new_frequency
print(answer2)