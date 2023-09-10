def main1(offsets):
    i = 0
    step_count = 0
    while i < len(offsets):
        jump = offsets[i]
        i_new = i + jump
        offsets[i] += 1
        i = i_new
        step_count += 1
    print(step_count)
    return


def main2(offsets):
    i = 0
    step_count = 0
    while i < len(offsets):
        jump = offsets[i]
        i_new = i + jump
        if jump >= 3:
            offsets[i] -= 1
        else:
            offsets[i] += 1
        i = i_new
        step_count += 1
    print(step_count)
    return


if __name__ == '__main__':
    with open('./input/day5.txt') as f:
        s = f.read()
        lines1 = [int(x) for x in s.strip().split('\n')]
        lines2 = [int(x) for x in s.strip().split('\n')]

    main1(lines1)
    main2(lines2)
