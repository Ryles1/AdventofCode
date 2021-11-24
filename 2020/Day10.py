#! python3
from math import prod, factorial


def initialize():
    with open('input-Day10.txt') as f:
        lines = f.read().strip().split('\n')

    adapter_ints = sorted([int(x) for x in lines])
    return adapter_ints


def count_diffs(adapter_list):
    one_count, three_count = 0, 0
    for i, v in enumerate(adapter_list):
        if i == len(adapter_list) - 1:
            continue
        elif adapter_list[i+1] - v == 3:
            three_count += 1
        elif adapter_list[i+1] - v == 1:
            one_count += 1
        else:
            pass
    return one_count, three_count


def check_arrangement(arrangement):
    for i, v in enumerate(arrangement):
        diff = adapter_list[i+1] - v
        if i == len(adapter_list) - 1:
            continue
        elif 0 < diff or diff > 3:
            return False
        else:
            continue
    return True


def count_arrangements(adapter_list):
    diffs, groups = [], []
    # get differences between each adapter
    diffs = [b-a for a, b in zip(adapter_list, adapter_list[1:])]
    j = 0
    # get groups of the same difference
    while j != len(diffs)-1:
        search_num = diffs[j]
        for k in range(j+1, len(diffs)):
            if diffs[k] != search_num:
                groups.append(k-j)
                j = k
                break
    #TODO: figure out how to calculate the right number of ways to organize

    product =  prod(group_arrangements)
    return product


if __name__ == '__main__':
    adapters = initialize()
    outlet_joltage = 0
    built_in = max(adapters) + 3
    adapters.insert(0, outlet_joltage)
    adapters.append(built_in)
    one_diffs, three_diffs = count_diffs(adapters)
    answer = one_diffs * three_diffs
    print(answer)
    num_ways = count_arrangements(adapters)
    print(num_ways)

