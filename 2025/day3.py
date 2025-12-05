def get_largest_joltage1(bank):
    first_largest, second_largest = 0, 0
    batteries = [int(x) for x in bank]
    first_largest = max(batteries[:-1]) #first digit cannot be last in the list
    first_largest_index = batteries[:-1].index(first_largest)
    second_largest = max(batteries[first_largest_index+1:])
    return first_largest * 10 + second_largest


def get_largest_joltage2(bank, num_batteries):
    batteries = [int(x) for x in bank]
    largest = [0 for n in range(num_batteries)]
    for i, battery in enumerate(batteries):
        if battery > min(largest): # only check if the joltage is larger than the smallest in the current total
            for index, digit in enumerate(largest):
                if battery > digit and len(largest) - index <= len(batteries) - i:  # prevent going out of bounds
                    largest[index] = battery
                    for n in range(index+1, num_batteries): # reset everything after digit that got replaced
                        largest[n] = 0
                    break
    return int(''.join([str(dig) for dig in largest]))


with open('./input/day3.txt') as f:
    banks = f.read().splitlines()

total = []
total2 = []
for bank in banks:
    largest_possible_joltage = get_largest_joltage1(bank)
    total.append(largest_possible_joltage)

    largest_12_joltages = get_largest_joltage2(bank, 12)
    total2.append(largest_12_joltages)

print(sum(total))
print(sum(total2))


