with open('./input/day5.txt') as f:
    lines = f.read()

range_lines, id_lines = lines.split('\n\n')
ranges = range_lines.split('\n')
available_IDs = [int(i) for i in id_lines.strip().split('\n')]

fresh_count = 0
fresh_ranges = []
for r in ranges:
    start_str, end_str = r.split('-')
    start = int(start_str)
    end = int(end_str)
    fresh_ranges.append((start, end))

fresh_ranges.sort(key=lambda rge: rge[0])

merge_ranges = []
for start, end in fresh_ranges:
    if not merge_ranges:
        merge_ranges.append([start, end])
    else:
        prev_start, prev_end = merge_ranges[-1]
        if prev_end >= start:  # if the last number in previous range overlaps the start of the next range,
            merge_ranges[-1][1] = max(end, prev_end) # change the end of prev range to the larger end value
        else:
            merge_ranges.append([start, end])  # if they don't overlap, can just add the current range to merged

for id in available_IDs:
    for mr in merge_ranges:
        if id in range(mr[0], mr[1]):
            fresh_count += 1

print(fresh_count)

total_fresh = 0
for mr in merge_ranges:
    total_fresh += (mr[1] - mr[0])+1

print(total_fresh)