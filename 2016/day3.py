def is_triangle(sides):
    int_sides = [int(side) for side in sides]
    int_sides.sort()
    if int_sides[0] + int_sides[1] > int_sides[2]:
        return True
    return False


def main(lines):
    triangle_count = 0
    for line in lines:
         if is_triangle(line):
            triangle_count += 1
    return triangle_count


def parse_part2(lines):
    triangles = []
    tri1, tri2, tri3 = [], [], []
    for line in lines:
        e1, e2, e3 = line
        tri1.append(e1)
        tri2.append(e2)
        tri3.append(e3)
        if len(tri1) == 3:
            triangles.extend([tri1, tri2, tri3])
            tri1, tri2, tri3 = [], [], []
    return triangles


if __name__ == '__main__':
    with open('./input/day3.txt') as f:
        instructions = f.read().strip().split('\n')
    instructions = [line.strip().split() for line in instructions]
    print(main(instructions))

    triangles2 = parse_part2(instructions)
    print(main(triangles2))

