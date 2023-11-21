from collections import Counter
from itertools import combinations


def main1(lines):
    twos = 0
    threes = 0
    counters = []
    for line in lines:
        counts = Counter(line)
        counters.append(counts)
        if 3 in counts.values():
            threes += 1
        if 2 in counts.values():
            twos += 1
    checksum = twos * threes
    combs = list(combinations(lines, 2))
    for comb in combs:
        num_diffs = 0
        diff_idx = 0
        for i, v in enumerate(comb[0]):
            if comb[1][i] != v:
                num_diffs += 1
                diff_idx = i
        if num_diffs == 1:
            answer = comb
            break
    box = [x for x in answer[0]]
    del box[diff_idx]
    answer = ''.join(box)

    return checksum, answer


if __name__ == '__main__':
    with open('./input/day2.txt') as f:
        lines = f.read().strip().split('\n')

    print(main1(lines))