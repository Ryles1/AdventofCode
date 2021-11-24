#! python3
import timeit


def part1(init):
    turn_tracker = dict()
    count, last_num = 0, 0
    for p in puzzle:
        count += 1
        turn_tracker[p] = {'spoken': 1, 'recent_turn': count, 'prev_turn': None}
        last_num = p
    next_num = last_num
    # TODO: definitely needs optimizing - took 20 min to run - consider using array of arrays instead
    while count != 2021:
        count += 1
        last_num = next_num
        if turn_tracker[last_num]['spoken'] == 1:
            next_num = 0
            turn_tracker[next_num]['prev_turn'] = turn_tracker[next_num]['recent_turn']
            turn_tracker[next_num]['recent_turn'] = count
            turn_tracker[next_num]['spoken'] += 1
            print(count, next_num)
            continue
        else:
            next_num = turn_tracker[last_num]['recent_turn'] - turn_tracker[last_num]['prev_turn']
            if next_num in turn_tracker.keys():
                turn_tracker[next_num]['prev_turn'] = turn_tracker[next_num]['recent_turn']
                turn_tracker[next_num]['recent_turn'] = count
                turn_tracker[next_num]['spoken'] += 1
                print(count, next_num)
                continue
            else:
                # next_num = turn_tracker[last_num]['recent_turn'] - turn_tracker[last_num]['prev_turn']
                turn_tracker[next_num] = {'spoken': 1, 'recent_turn': count, 'prev_turn': None}
                print(count, next_num)
                continue
    print(last_num)


def part2(init):
    count, last_num = 0,0
    spoken = [x for x in init]

    for i in range(len(spoken)+1, 2020):
        if spoken.count(spoken[-1]) == 1:
            spoken.append(0)
        else:
            new_num = i - spoken.index(spoken[-1])
            spoken.append(new_num)
    print(spoken[-1])

if __name__ == '__main__':
    puzzle = [15,5,1,4,7,0]
    part1(puzzle)

