import re, math


STARTING_SPEED = 0
SPEED_INCREASE = 1


def parse_input(s, part2=False):
    nums = re.findall(r'\d+', s)
    if part2:
        race_data = [int(''.join(nums))]
    else:
        race_data = [int(num) for num in nums]
    return race_data


def get_distance(tt, th):
    travel_time = tt - th
    speed = th
    return speed * travel_time


def main(lines, part2=False):
    times_str, distances_str = lines[0], lines[1]
    times = parse_input(times_str, part2)
    distances = parse_input(distances_str, part2)
    races = list(zip(times, distances))
    win_options = []
    for race in races:
        total_time = race[0]
        current_record = race[1]
        wins = 0
        for hold_time in range(1, total_time):
            travel_distance = get_distance(total_time, hold_time)
            if travel_distance > current_record:
                wins += 1
        win_options.append(wins)

    return math.prod(win_options)


if __name__ == '__main__':
    with open('./input/day6.txt') as f:
        lines = f.readlines()

    answer1 = main(lines)
    print(answer1)
    answer2 = main(lines, True)
    print(answer2)
