def main(seq: str, increment):
    count: int = 0
    for i, v in enumerate(seq):
        if i == len(seq) - 1:
            if increment == 1:
                comparison_value = seq[0]
            else:
                comparison_value = seq[increment]
            if v == comparison_value:
                count += int(v)
        else:
            if i + increment >= len(seq):
                if v == seq[i + increment - len(seq)]:
                    count += int(v)
            elif v == seq[i + increment]:
                count += int(v)
    return count


if __name__ == '__main__':
    with open('./input/day1.txt') as f:
        sequence = f.read().strip()

    print(main(sequence, 1))
    print(main(sequence, len(sequence)//2))
