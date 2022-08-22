import itertools


def populate_happiness(lines):
    happy_dict = dict()
    for line in lines:
        parts = line.strip().strip('.').split()
        person = parts[0]
        neighbor = parts[-1]
        positive = True if parts[2] == 'gain' else False
        value = int(parts[3]) * 1 if positive else int(parts[3]) * -1
        happy_dict.setdefault(person, {})
        happy_dict[person][neighbor] = value
    return happy_dict


def calculate_happiness(arrangement, happiness_dict):
    happiness = 0
    arrangement_list = list(arrangement)
    for i, person in enumerate(arrangement_list):
        if i == 0:
            left_person = arrangement_list[-1]
            right_person = arrangement[i + 1]
        elif i == len(arrangement_list) - 1:
            left_person = arrangement_list[i - 1]
            right_person = arrangement[0]
        else:
            left_person = arrangement_list[i - 1]
            right_person = arrangement_list[i + 1]
        happiness += happiness_dict[person][left_person]
        happiness += happiness_dict[person][right_person]
    return happiness


def add_self(d):
    d['self'] = {}
    for person in d.keys():
        if person == 'self':
            continue
        d['self'][person] = 0
        d[person]['self'] = 0
    return d


def main(lines, part2=False):
    happiness_dict = populate_happiness(lines)
    if part2:
        happiness_dict = add_self(happiness_dict)
    permutations = itertools.permutations(happiness_dict.keys())
    optimal_arrangement = (None, 0)
    for p in permutations:
        current_happiness = calculate_happiness(p, happiness_dict)
        if current_happiness > optimal_arrangement[1]:
            optimal_arrangement = (p, current_happiness)
    return optimal_arrangement


if __name__ == '__main__':
    with open('./input/day13.txt') as f:
        lines = f.readlines()

    print(main(lines))
    print(main(lines, True))
