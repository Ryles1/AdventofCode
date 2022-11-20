import heapq, csv
from collections import deque


FAV_NUM = 1364
DEST_COL = 31
DEST_ROW = 39
START_COL = 1
START_ROW = 1
OPEN = '.'
WALL = '#'


def generate_map(x, y):
    map_matrix = []
    # calculate for two extra rows and columns in case
    # the shortest route is not a direct line and requires to backtrack
    for row in range(y + 2):
        map_matrix.append([])
        for col in range(x + 2):
            number = col**2 + 3*col + 2*col*row + row + row**2 + FAV_NUM
            binary_number = str(bin(number)[2:])
            num_bits = binary_number.count('1')
            if num_bits % 2 == 0:
                map_matrix[row].append(OPEN)
            else:
                map_matrix[row].append(WALL)
    return map_matrix


def get_adjacent_coord(adjustment, location):
    new_row = location[0] + adjustment[0]
    new_col = location[1] + adjustment[1]
    return new_row, new_col


def get_adjacents(matrix):
    # cannot move diagonally
    adjacency_dict = {}
    max_row = len(matrix)
    max_col = len(matrix[0])
    adjustments = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            adjacency_dict[(i, j)] = {}
            for adjustment in adjustments:
                adjacent = get_adjacent_coord(adjustment, (i, j))
                if 0 <= adjacent[0] < max_row and 0 <= adjacent[1] < max_col:
                    adjacent_value = matrix[adjacent[0]][adjacent[1]]
                    # do not include walls
                    if adjacent_value == OPEN:
                        adjacency_dict[(i, j)][adjacent] = matrix[adjacent[0]][adjacent[1]]
    return adjacency_dict


def heuristic(current, target):
    # manhattan distance
    distance_to_target = abs(target[0] - current[0]) + abs(target[1] - current[1])
    return distance_to_target


def a_star(adj, start, end):
    frontier = [[0, start]]
    came_from = dict()
    came_from[start] = None
    cost = dict()
    cost[start] = 0
    while frontier:
        heapq.heapify(frontier)
        current_cost, current = heapq.heappop(frontier)

        if current == end:
            break

        for next_node in adj[current].keys():
            new_cost = cost[current] + 1
            if next_node not in cost or new_cost < cost[next_node]:
                cost[next_node] = new_cost
                priority = new_cost + heuristic(next_node, end)
                heapq.heappush(frontier, [priority, next_node])
                came_from[next_node] = current
    return cost, came_from


def get_path(dirs, start, end):
    current = end
    path = []
    while current != start:
        path.append(str(current))
        current = dirs[current]
    path.append(str(start))
    path.reverse()
    return path


def bfs(adj, start, end):
    visited = set()
    frontier = deque([start])
    cost = dict()
    cost[start] = 0
    while frontier:
        current = frontier.popleft()
        visited.add(current)

        for next_node in adj[current].keys():
            if next_node not in visited:
                frontier.append(next_node)
            new_cost = cost[current] + 1
            if next_node not in cost:
                cost[next_node] = new_cost
    return cost


def main():
    map_matrix = generate_map(DEST_COL, DEST_ROW)
    adjacents = get_adjacents(map_matrix)
    start = (START_ROW, START_COL)
    end = (DEST_ROW, DEST_COL)
    a_star_cost, a_star_dirs = a_star(adjacents, start, end)
    a_star_path = get_path(a_star_dirs, start, end)
    print(f'A* cost: {a_star_cost[end]}')

    new_map = generate_map(50, 50)
    new_adjacents = get_adjacents(new_map)
    all_costs = bfs(new_adjacents, start, end)
    num_under_fifty = 0
    for n, c in all_costs.items():
        if c <= 50:
            num_under_fifty += 1

    # generate csv of each cost for checking
    with open('day13.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for k, v in all_costs.items():
            writer.writerow([str(k), v])
    # generate csv map for viewing in excel - flawed
    with open('day13map.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for i, row in enumerate(new_map):
            new_row = []
            for j, col in enumerate(row):
                if (i, j) in all_costs:
                    new_row.append(str(all_costs[(i, j)]))
                else:
                    new_row.append(col)
            writer.writerow(''.join(new_row))

    print(f'Number of nodes in 50 steps or less = {num_under_fifty}')
    return


if __name__ == '__main__':
    print(main())
