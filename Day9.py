#! python3
from collections import deque
import itertools


def initialize():
    with open('input-Day9.txt') as f:
        lines = f.read().strip().split('\n')

    number_gen = (int(line) for line in lines)
    number_tup = tuple([int(line) for line in lines])

    stack = deque()
    for i in range(25):
        stack.append(next(number_gen))
    return number_gen, stack, number_tup


def check_number(check_num, check_dq):
    combs = itertools.combinations(check_dq, 2)
    check = list(filter(lambda x: x[0] + x[1] == check_num, combs))
    return True if check else False

def part_1(numbers, stack):
    while True:
        next_num = next(numbers)
        if not check_number(next_num, stack):
            return next_num
        else:
            stack.popleft()
            stack.append(next_num)


def get_contig(total, set):
    for i in range(len(set)):
        for j in range(len(set[i+1:])):
            if sum(set[i:j]) == total:
                return set[i:j]
            elif sum(set[i:j]) > total:
                break
    return subset

def part_2(invalid, nums):
    subset = get_contig(invalid, nums)
    return min(subset) + max(subset)

if __name__ == '__main__':
    num_gen, stack, num_tup = initialize()
    invalid_num = part_1(num_gen, stack)
    print(f'Answer to part 1 is {invalid_num}')
    weakness = part_2(invalid_num, num_tup)
    print(f'Answer to part 2 is {weakness}')