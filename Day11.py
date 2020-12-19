#! python3
import copy


def get_neighbors(grid, row, column):
    max_row = len(grid)
    max_col = len(grid[0])
    temp_neighbors = []
    for i in range(row-1, row+2):
        for j in range(column-1, column+2):
            if i == row and j == column:
                continue
            else:
                temp_neighbors.append((i, j))
    return list(filter(lambda x: x[0] >= 0 and x[0] < max_row and x[1] >=0 and x[1] < max_col, temp_neighbors))


def check_change(neighbors, current, grid):
    global occupied, empty
    occupied_neighbors = len(list(filter(lambda y: grid[y[0]][y[1]] == '#', neighbors)))
    if current == occupied and occupied_neighbors >= 4:
        return True
    elif current == empty and occupied_neighbors == 0:
        return True
    else:
        return False


def update(start_grid):
    old_grid = []
    new_grid = copy.deepcopy(start_grid)
    change = False
    #TODO:  figure out why this loop never breaks out
    while True:
        old_grid = copy.deepcopy(new_grid)
        for i in range(len(old_grid)):
            for j in range(len(old_grid[i])):
                current_seat = old_grid[i][j]
                if current_seat == '.':
                    continue
                neighbors = get_neighbors(old_grid,i,j)
                change = check_change(neighbors, current_seat, old_grid)
                if change and current_seat == empty:
                    new_grid[i][j] = occupied
                    print(f' changing {i}, {j}')
                elif change and current_seat == occupied:
                    new_grid[i][j] = empty
                    print(f' changing {i}, {j}')
                else:
                    new_grid[i][j] = current_seat
        if old_grid == new_grid:
            break
    return new_grid


if __name__ == '__main__':
    with open('input-Day11.txt') as f:
        start_grid = [[j for j in i] for i in f.read().strip().split('\n')]
    empty = 'L'
    occupied = '#'
    ground = '.'
    final_grid = update(start_grid)
    num_seats = sum([x.count('#') for x in final_grid])
    print(f'Number of occupied seats at end of part 1 is {num_seats}')

