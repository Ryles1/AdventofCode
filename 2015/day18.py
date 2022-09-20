import copy

ON = '#'
OFF = '.'


def get_neighbors(row, column, grid):
    """Returns a list of neighbors inside the grid."""
    max_row = len(grid)
    max_col = len(grid[0])
    possible_neighbors = []
    # populate the (row, col) of all adjacent locations - no diagonals though
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if i == row and j == column:
                continue
            possible_neighbors.append((i, j))
    # x below is a (row, col) tuple for neighbors around the location in question
    # filter is used to avoid IndexErrors from going outside the matrix edges
    neighbors = list(filter(lambda x: 0 <= x[0] < max_row and 0 <= x[1] < max_col, possible_neighbors))
    return neighbors


def count_lights(grid):
    on = 0
    for row in grid:
        on += row.count(ON)
    return on


def update_grid(grid, part2):
    new_grid = [[OFF for r in range(len(grid[0]))] for _ in grid]
    for m, row in enumerate(grid):
        for n, col in enumerate(row):
            on_nearby = 0
            neighbors = get_neighbors(m, n, grid)
            for neighbor in neighbors:
                if grid[neighbor[0]][neighbor[1]] == ON:
                    on_nearby += 1
            if col == OFF and on_nearby == 3:
                new_grid[m][n] = ON
            elif col == ON:
                if 2 <= on_nearby <= 3:
                    new_grid[m][n] = ON
                else:
                    new_grid[m][n] = OFF
    if part2:
        new_grid[0][0] = ON
        new_grid[0][len(grid) - 1] = ON
        new_grid[len(grid) - 1][0] = ON
        new_grid[len(grid) - 1][len(grid) - 1] = ON
    return new_grid


def main(grid, steps, part2=False):
    current_grid = grid
    for step in range(steps):
        updated_grid = update_grid(current_grid, part2)
        current_grid = copy.deepcopy(updated_grid)
    lights_on = count_lights(current_grid)
    return lights_on


if __name__ == '__main__':
    with open('./input/day18.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    g = [[x for x in row] for row in lines]
    print(main(g, 100))
    g2 = copy.deepcopy(g)
    g2[0][0] = ON
    g2[0][99] = ON
    g2[99][0] = ON
    g2[99][99] = ON

    print(main(g2, 100, True))
