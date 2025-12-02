def is_invalid_id1(id_num: str):
    id_length = len(id_num)
    first_half = id_num[:id_length//2]
    second_half = id_num[id_length//2:]
    if first_half == second_half:
        return True
    return False


def is_invalid_id2(id_num: str, divisor):
    segments = []
    id_length = len(id_num)
    seg_length = divisor
    for i in range(0, id_length, seg_length):
        segments.append(id_num[i:i+seg_length])
    if all(s == segments[0] for s in segments):
        return True
    return False


with open('./input/day2.txt') as f:
    id_ranges = f.read().split(',')

invalid_ids_p1 = []
invalid_ids_p2 = []

for id_range in id_ranges:
    start, end = (int(x) for x in id_range.split('-'))

    for product_id in range(start, end + 1):
        str_id = str(product_id)
        if len(str_id) % 2 != 0:
            continue
        elif is_invalid_id1(str_id):
            invalid_ids_p1.append(product_id)

    for product_id in range(start, end + 1):
        str_id = str(product_id)
        divisors = []
        id_length = len(str_id)
        for l in range(1, id_length):
            if id_length % l == 0:
                divisors.append(l)

        for divisor in divisors:
            if is_invalid_id2(str_id, divisor):
                invalid_ids_p2.append(product_id)
                break

print(sum(invalid_ids_p1))
print(sum(invalid_ids_p2))

