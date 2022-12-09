from math import prod


def visible_on_row(r, c, height):
    if height > max(r[:c]) or height > max(r[c + 1:]):
        return True
    return False


def visible_on_col(m, r, c, part2=False):
    height = m[r][c]
    top = []
    bottom = []
    for row_index, row in enumerate(m):
        if row_index < r:
            top.append(row[c])
        if row_index > r:
            bottom.append(row[c])
    if part2:
        return top, bottom
    if height > max(top) or height > max(bottom):
        return True
    return False


def part1(hmap):
    visible = 0
    for i, row in enumerate(hmap):
        for j, tree_height in enumerate(row):
            if i in (0, len(hmap) - 1) or j in (0, len(row) - 1):
                visible += 1
                continue
            else:
                if visible_on_row(row, j, tree_height) or visible_on_col(hmap, i, j):
                    visible += 1
    return visible


def count_visible_trees(l, r, t, b, h):
    left, right, top, bottom = 0, 0, 0, 0
    # reverse l since left was started from edge of map
    for tree in l[::-1]:
        if tree < h:
            left += 1
        elif tree >= h:
            left += 1
            break
    for tree in r:
        if tree < h:
            right += 1
        elif tree >= h:
            right += 1
            break
    # reverse t since top was started from edge of map
    for tree in t[::-1]:
        if tree < h:
            top += 1
        elif tree >= h:
            top += 1
            break
    for tree in b:
        if tree < h:
            bottom += 1
        elif tree >= h:
            bottom += 1
            break
    return left, right, top, bottom


def part2(hmap):
    best_score = 0
    for i, row in enumerate(hmap):
        for j, tree_height in enumerate(row):
            left = row[:j]
            right = row[j + 1:]
            top, bottom = visible_on_col(hmap, i, j, True)
            visible_trees = count_visible_trees(left, right, top, bottom, tree_height)
            score = prod(visible_trees)
            best_score = score if score > best_score else best_score
    return best_score


if __name__ == '__main__':
    FILENAME = './input/day8.txt'
    with open(FILENAME) as f:
        lines = f.readlines()
        heightmap = [[int(x) for x in row if x.isdigit()] for row in lines]

    print(part1(heightmap))
    print(part2(heightmap))
