#! python3
from math import prod

with open('input.txt') as f:
    lines = f.readlines()

map = []
for line in lines:
    map.append(list(line.strip()))

print('length of map is', len(map))

tree = '#'
trees = []

width = len(map[0])

def count_trees(slope_tuple):
    right, down = slope_tuple[0], slope_tuple[1]
    global width, tree, map
    row, col = 0, 0
    tree_count = 0
    while row <= len(map) - 1:
        if col >= width:
            col = col - width
        #print(row, col)
        if map[row][col] == tree:
            tree_count += 1
        row += down
        col += right
    return tree_count

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for i, slope in enumerate(slopes):
    tree_temp = (count_trees(slope))
    print(f'tree count in slope {i} is {tree_temp}')
    trees.append(tree_temp)
    

print(prod(trees))
