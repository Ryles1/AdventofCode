NEIGHBORS = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
PAPER = '@'
REMOVED = 'x'
EMPTY = '.'

with open('./input/day4.txt') as f:
    grid = f.read().strip().split('\n')

accessible = []
start_grid = {}

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        adjacent_count = 0
        if col != PAPER:
            start_grid[(i, j)] = EMPTY
            continue
        for neighbor in NEIGHBORS:
            if i+neighbor[0] in (-1, len(grid)) or j+neighbor[1] in (-1, len(row)):
                continue
            elif grid[i+neighbor[0]][j+neighbor[1]] == PAPER:
                adjacent_count += 1
        if adjacent_count < 4:
            accessible.append((i, j))
        # convert into a dict for part 2
        start_grid[(i, j)] = PAPER

print(len(accessible))

# part 1 was the first round of identifying accessible rolls
# now update start_grid for the identified accessible rolls by changing them to an x
# and update the counter for how many were removed this round

part2_count = len(accessible)
for roll in accessible:
    start_grid[roll] = REMOVED

# then clear accessible to use again in next round

accessible.clear()

# use a while loop to keep the process running until no rolls are able to be removed
roll_removed = True
round = 2
while roll_removed:
    roll_removed = False
    for k, v in start_grid.items():
        adjacent_count = 0
        if v != PAPER:
            continue
        for neighbor in NEIGHBORS:
            if k[0] + neighbor[0] in (-1, len(grid)) or k[1] + neighbor[1] in (-1, len(grid[k[0]])):
                continue
            elif start_grid[(k[0] + neighbor[0], k[1] + neighbor[1])] == PAPER:
                adjacent_count += 1
        if adjacent_count < 4:
            accessible.append(k)
    if len(accessible) > 0:
        roll_removed = True
        part2_count += len(accessible)

        for roll in accessible:
            start_grid[roll] = REMOVED
        accessible.clear()
    round += 1
    print(f'Round {round}')

print(part2_count)
