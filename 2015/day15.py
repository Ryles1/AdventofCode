import itertools

NUM_SPOONS = 100


def parse_lines(l):
    data = {}
    for line in l:
        parts = line.split()
        ingredient = parts[0].strip(':')
        data[ingredient] = {'capacity': 0,
                            'durability': 0,
                            'flavor': 0,
                            'texture': 0,
                            'calories': 0}
        data[ingredient]['capacity'] = int(parts[2].strip(','))
        data[ingredient]['durability'] = int(parts[4].strip(','))
        data[ingredient]['flavor'] = int(parts[6].strip(','))
        data[ingredient]['texture'] = int(parts[8].strip(','))
        data[ingredient]['calories'] = int(parts[10].strip(','))
    return data


def main(lines):
    properties = parse_lines(lines)
    score = 0
    for i in range(1,101):
        for j in range(1, 101 - i):
            for k in range(1, 101 - i - j):
                l = 100 - i - j - k
                calories = sum([properties[ing]['calories'] * x for ing, x in zip(properties, (i, j, k, l))])
                if calories != 500:
                    continue
                c_score = sum([properties[ing]['capacity'] * x for ing, x in zip(properties, (i, j, k, l))])
                d_score = sum([properties[ing]['durability'] * x for ing, x in zip(properties, (i, j, k, l))])
                f_score = sum([properties[ing]['flavor'] * x for ing, x in zip(properties, (i, j, k, l))])
                t_score = sum([properties[ing]['texture'] * x for ing, x in zip(properties, (i, j, k, l))])
                if not all(map(lambda x: x > 0, (c_score, d_score, f_score, t_score))):
                    continue
                comb_score = c_score * d_score * f_score * t_score

                score = comb_score if comb_score > score else score
    return score


if __name__ == '__main__':
    with open('./input/day15.txt') as f:
        lines = [i.strip() for i in f.readlines()]

    print(main(lines))
