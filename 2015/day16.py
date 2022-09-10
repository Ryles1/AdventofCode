message = {'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1
           }


def parse_lines(lines):
    sue_dict = {}
    for line in lines:
        sue_number = line[4: line.index(':')]
        sue_dict[sue_number] = {k: 0 for k in message.keys()}
        for key in message.keys():
            if key in line:
                start = line.find(key) + len(key) + 2
                value = int(line[start: start + 2].strip(',').strip('\n'))
                sue_dict[sue_number][key] = value
    return sue_dict


def main(lines, part2=False):
    sue_dict = parse_lines(lines)
    sue_with_most_matches = ('', 0)
    for sue_num, sue_data in sue_dict.items():
        matches = 0
        for k, v in message.items():
            if part2 and k == 'cats' and sue_data.get('cats', -1) > v:
                matches += 1
            elif part2 and k == 'trees' and sue_data.get('trees', -1) > v:
                matches += 1
            elif part2 and k == 'pomeranians' and sue_data.get('pomeranians', -1) < v:
                matches += 1
            elif part2 and k == 'goldfish' and sue_data.get('goldfish', -1) < v:
                matches += 1
            elif sue_data[k] == v:
                matches += 1
        if matches > sue_with_most_matches[1]:
            sue_with_most_matches = (sue_num, matches)
    return sue_with_most_matches


if __name__ == '__main__':
    with open('./input/day16.txt') as f:
        lines = [i.strip() for i in f.readlines()]

    print(main(lines))
    print(main(lines, True))
