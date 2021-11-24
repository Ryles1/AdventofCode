#! python3

if __name__ == '__main__':
    with open('input-Day17.txt') as f:
        start_grid = [[j for j in i] for i in f.read().strip().split('\n')]
    active = '#'
    inactive = '.'
    final_grid = update(start_grid)
    num_seats = sum([x.count('#') for x in final_grid])
    print(f'Number of occupied seats at end of part 1 is {num_seats}')