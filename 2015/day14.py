import pprint
RACE_TIME = 2503


def part1(lines):
    reindeer_data = {}

    for line in lines:
        parts = line.strip().strip('.').split()
        reindeer = parts[0]
        reindeer_data[reindeer] = {'score': 0,
                     'distance': 0}
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[-2])
        reindeer_data[reindeer]['speed'] = speed
        reindeer_data[reindeer]['fly_time'] = fly_time
        reindeer_data[reindeer]['rest_time'] = rest_time
        cycle_time = fly_time + rest_time
        reindeer_data[reindeer]['cycle_time'] = cycle_time
        cycles = RACE_TIME // cycle_time
        partial_cycle_time = RACE_TIME % cycle_time
        partial_cycle_distance = speed * fly_time if partial_cycle_time > fly_time else speed * partial_cycle_time
        race_distance = cycles * speed * fly_time + partial_cycle_distance
        reindeer_data[reindeer]['race_distance'] = race_distance
    return reindeer_data


def part2(reindeer_data):

    for sec in range(1, RACE_TIME+1):
        leader = []
        for reindeer in reindeer_data:
            if 0 < sec % reindeer_data[reindeer]['cycle_time'] <= reindeer_data[reindeer]['fly_time']:
                reindeer_data[reindeer]['distance'] += reindeer_data[reindeer]['speed']
            if len(leader) == 0 or reindeer_data[leader[0]]['distance'] < reindeer_data[reindeer]['distance']:
                leader = [reindeer]
            elif reindeer_data[leader[0]]['distance'] == reindeer_data[reindeer]['distance']:
                leader.append(reindeer)
            else:
                continue
        for l in leader:
            reindeer_data[l]['score'] += 1
    return reindeer_data



if __name__ == '__main__':
    with open('./input/day14.txt') as f:
        lines = f.readlines()

    data = part1(lines)
    winner = sorted(data.items(), key=lambda item: item[1]['race_distance'], reverse=True)
    print(winner[0])
    part2_data = part2(data)
    winner2 = sorted(data.items(), key=lambda item: item[1]['score'], reverse=True)
    print(winner2[0])
