#! python3


def get_dims(present):
    length, width, height = present.split("x")
    return int(length), int(width), int(height)


def shortest_perimeter(l, w, h):
    dims = sorted([l, w, h])[:2]
    return 2 * dims[0] + 2 * dims[1]


with open("./input/2015day2input.txt") as f:
    presents = f.read().split("\n")

total_ribbon = 0

for present in presents:
    length, width, height = get_dims(present)
    min_perimeter = shortest_perimeter(length, width, height)
    # TODO: need smallest side face to compare with
    volume = length * width * height
    total_ribbon += min_perimeter + volume

print(total_ribbon)
