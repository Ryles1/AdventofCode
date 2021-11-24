#! python3
from copy import deepcopy

def find_destination(curr_value, circle):
    min_value = min(circle)
    max_value = max(circle)
    dest = None
    while True:
        dest = curr_value - 1
        if dest < min_value:
            dest = max_value
            return dest
        elif dest not in circle:
            curr_value -= 1
            continue
        else:
            return dest


def part1(nums):
    current_idx = 0
    for _ in range(100):
        #need to fix if current index is close to end of nums
        first_idx = current_idx + 1 if current_idx != len(nums) -1 else 0
        last_idx = current_idx + 4 if current_idx != len(nums) -1 else 3
        moving_cups = nums[first_idx: last_idx]
        remaining_cups = nums[:first_idx] + nums[last_idx:]
        dest_value = find_destination(nums[current_idx], remaining_cups)
        #get index from list with cups removed
        dest_idx = remaining_cups.index(dest_value)+1
        #fill in how to reinsert the cups
        for i, j in zip(moving_cups, (dest_idx, dest_idx+1, dest_idx+2)):
            remaining_cups.insert(j, i)
        nums = deepcopy(remaining_cups)
        #this should be last step before next loop
        current_idx += 1
        if current_idx == len(nums):
            current_idx = 0
    return nums


if __name__ == '__main__':
    input_text = '784235916'
    input_list = [int(x) for x in input_text]
    final_part1 = part1(input_list)
    answer1 = final_part1[final_part1.index(1):] + final_part1[:final_part1.index(1)]
    print(''.join([str(x) for x in answer1 if x != 1]))
