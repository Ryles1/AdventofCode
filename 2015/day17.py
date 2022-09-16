from itertools import combinations


def determine_max_bins(b):
    b_ascending = sorted(b)
    sum = 0
    for i, bin in enumerate(b_ascending):
        sum += bin
        if sum > 150:
            return i + 1
    return i + 1


def determine_min_bins(b):
    b_descending = sorted(b, reverse=True)
    sum = 0
    for i, bin in enumerate(b_descending):
        sum += bin
        if sum > 150:
            return i + 1
    return i + 1


def main(bin_list):
    bins = sorted([int(b) for b in bin_list])
    max_bins = determine_max_bins(bins)
    min_bins = determine_min_bins(bins)
    fitting_combs = 0
    num_min_len_combs = 0
    for r in range(min_bins, max_bins + 1):
        combs = combinations(bins, r)
        for c in combs:
            s = sum(c)
            if s == 150:
                fitting_combs += 1
                if r == min_bins:
                    num_min_len_combs += 1
    return fitting_combs, num_min_len_combs


if __name__ == '__main__':
    with open('./input/day17.txt') as f:
        bin_list = f.read().strip().split('\n')

    print(main(bin_list))
