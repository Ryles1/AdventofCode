def parse(lines):
    crate_rows = {k: [] for k in range(1, 10)}
    lines_split = lines.split('\n')
    for i, line in enumerate(lines_split[::-1]):  # last line is just column labels
        if i == 0:
            continue
        for j in range(1, 36, 4):
            if line[j].isalpha():
                crate_rows[i].append(line[j])
            else:
                crate_rows[i].append('.')
    #convert the dict of rows into a dict of "columns" (crate stacks)
    # crate stacks are numbered 1 to 9
    crate_stacks = {k: [] for k in range(1, 10)}
    for row, crates in crate_rows.items():
        for i, crate in enumerate(crates):
            if crate != '.':
                crate_stacks[i + 1].append(crate)  # i+1 accounts for 1-indexed stacks
    return crate_stacks


def main(crates, instructions_string, part1=True):
    instructions = instructions_string.strip().split('\n')
    for line in instructions:
        parts = line.strip().split()
        num_crates = int(parts[1])
        from_stack = int(parts[-3])
        to_stack = int(parts[-1])

        # get temp list and reversed list of crates from starting stack
        crates_to_move = crates[from_stack][(-num_crates):]
        if part1:
            crates_to_move = crates_to_move[::-1]

        # remove the crates from the starting stack
        for _ in range(num_crates):
            crates[from_stack].pop()

        # append the crates to the destination stack
        crates[to_stack].extend(crates_to_move)

    message = ''.join([crates[k][-1] for k in crates.keys()])
    return message

if __name__ == '__main__':
    with open('./input/day5.txt') as f:
        raw = f.read()

    arrangement, instructions_raw = raw.split('\n\n')
    starting_crates = parse(arrangement)

    print(main(starting_crates, instructions_raw))
    part2_crates = parse(arrangement)
    print(main(part2_crates, instructions_raw, False))

