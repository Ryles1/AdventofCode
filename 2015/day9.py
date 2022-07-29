import itertools


def main(lines):
    locations = set()
    distances = {}
    routes = {}
    for line in lines:
        split = line.split()
        start = split[0]
        end = split[2]
        distance = int(split[-1])
        locations.add(start)
        locations.add(end)
        distances.setdefault(start, {})
        distances.setdefault(end, {})
        distances[start][end] = distance
        distances[end][start] = distance

    perms = itertools.permutations(locations)
    max_route = ([],0)
    min_route = ([], 10000000)
    for perm in perms:
        route_distance = 0
        for i, loc in enumerate(perm):
            if i == len(perm) - 1:  # terminate before the index error
                break
            l2 = perm[i + 1]
            leg_dist = distances[loc][l2]
            route_distance += leg_dist
        routes[tuple(perm)] = route_distance
        if route_distance > max_route[1]:
            max_route = (perm, route_distance)
        if route_distance < min_route[1]:
            min_route = (perm, route_distance)
    print(max(routes.values()))
    print(min(routes.values()))
    return max_route, min_route


if __name__ == '__main__':
    with open('./input/day9.txt') as f:
        lines = f.readlines()

    print(main(lines))
