import copy


def get_redist_idx(banks):
    max_idx = banks.index(max(banks))
    return max_idx


def main(banks):
    start_bank = copy.deepcopy(banks)
    new_banks = [x for x in banks]
    count = 0
    sequences = set()  # for tracking sequences
    sequence_cycles = dict()  # for tracking the cycle sequences are discovered in
    while ','.join([str(y) for y in new_banks]) not in sequences:
        new_sequence = ','.join([str(y) for y in new_banks])
        sequences.add(new_sequence)
        sequence_cycles[new_sequence] = count
        redist_bank_idx = get_redist_idx(new_banks)
        redist_val = new_banks[redist_bank_idx]
        new_banks[redist_bank_idx] = 0
        # redistribute redist_val to each index
        i = redist_val
        j = redist_bank_idx + 1 if (redist_bank_idx + 1) < len(new_banks) else 0
        while i > 0:
            new_banks[j] += 1
            i -= 1
            j += 1
            if j > len(new_banks) - 1:
                j = 0
        count += 1
    # number of cycles between repeat cycles will be the total count less the cycle it was first discovered
    return count, count - sequence_cycles[','.join(str(k) for k in new_banks)]


if __name__ == '__main__':
    starting_string = '0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11'

    start_banks = [int(x) for x in starting_string.split('\t')]

    print(main(start_banks))
