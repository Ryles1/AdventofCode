import itertools
from math import prod


def main(num_groups, packages):
    # each group has to be equal weight
    total_weight = sum(packages)
    reqd_group_weight = total_weight // num_groups

    for i in range(len(packages)):
        # get only combinations of packages that match the required weight
        combs = [c for c in (itertools.combinations(packages, i)) if sum(c) == reqd_group_weight]

        if combs:
            # if combs exist, this is the minimum number of packages that can be in the passenger area
            # sort the combinations by minimum quantum entanglement (product)
            options = sorted(combs, key=prod)
            return prod(options[0])


if __name__ == '__main__':
    with open('./input/day24.txt') as f:
        lines = [int(i) for i in f.readlines()]

    print(main(3, lines))
    print(main(4, lines))
