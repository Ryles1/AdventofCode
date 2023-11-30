import csv

def parse_claims(lines):
    claim_dict = {}
    for line in lines:
        parts = line.split()
        claim_num = int(parts[0][1:])
        claim_dict[claim_num] = {}
        claim_dict[claim_num]['coord'] = list(map(int, parts[2].strip(':').split(',')))
        claim_dict[claim_num]['size'] = list(map(int, parts[3].split('x')))
    return claim_dict


def main1(lines):
    claims = parse_claims(lines)
    fabric = [[0 for _ in range(1001)] for i in range(1001)]
    for claim_num, claim_info in claims.items():
        x_start = claim_info['coord'][0]
        y_start = claim_info['coord'][1]
        width = claim_info['size'][0]
        depth = claim_info['size'][1]
        x_end = x_start + width
        y_end = y_start + depth
        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                try:
                    fabric[y][x] += 1
                except IndexError:
                    print(f'x={x}, y={y}')
                    raise IndexError
    overlapping = 0
    for row in fabric:
        for col in row:
            overlapping += 1 if col >= 2 else 0
    # part 2
    intact_claim = 0
    claim_found = False
    for claim_num, claim_info in claims.items():
        if claim_found:
            break
        x_start = claim_info['coord'][0]
        y_start = claim_info['coord'][1]
        width = claim_info['size'][0]
        depth = claim_info['size'][1]
        x_end = x_start + width
        y_end = y_start + depth
        intact_claim = claim_num
        for y in range(y_start, y_end):
            if intact_claim == 0:
                break
            for x in range(x_start, x_end):
                if fabric[y][x] != 1:
                    intact_claim = 0
                    break
            if y == y_end - 1 and intact_claim != 0:
                claim_found = True
                break
    return overlapping, intact_claim


if __name__ == '__main__':
    with open('./input/day3.txt') as f:
        lines = f.read().strip().split('\n')

    print(main1(lines))