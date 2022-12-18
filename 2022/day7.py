class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent


def get_total_size(start, under_size, max_size):
    """Recursively traverse the tree.
    Calculate size of each directory at each recursive step by summing the sizes
    of the child nodes, and add them to the under_size list to keep track of each dir and size.
    Can specify max_size of directories to track."""
    size = 0
    for child in start.children:
        if isinstance(child, File):
            size += child.size
        else:
            new = get_total_size(child, [], max_size)
            new_size = new[0]
            size += new_size
            under_size.extend(new[1])
    if size <= max_size:
        under_size.append((start, size))
    return size, under_size


def find_dir(start, destination):
    for child in start.children:
        if child.name == destination:
            return child
    for child in start.children:
        if isinstance(child, File):
            continue
        found_child = find_dir(child, destination)
        if found_child:
            return found_child
    return None


def main(lines, total_space, update_size):
    current_dir = None
    root = None
    for line in lines:
        if line.split()[1] == 'cd':
            change_dir = line.split()[-1]
            if change_dir == '/':
                root = Directory(change_dir, None)
                current_dir = root
            elif change_dir == '..':
                current_dir = current_dir.get_parent()
            else:
                # 'cd' only changes to children of current directory, so search parent
                current_dir = find_dir(current_dir, change_dir)
        elif line.split()[1] == 'ls':
            continue
        elif line.split()[0] == 'dir':
            # add new directory to children list of parent directory
            dir_name = line.split()[-1]
            current_dir.add_child(Directory(dir_name, current_dir))
        elif line.split()[0].isnumeric():
            # add new file to children list of parent directory
            size, filename = line.split()
            size = int(size)
            current_dir.add_child(File(filename, size, current_dir))
    part1 = get_total_size(root, [], 100_000)
    p1answer = sum([c[1] for c in part1[1]])

    part2 = get_total_size(root, [], total_space)  # sizes of all directories
    root_size, dir_list = part2  # unpack
    unused = total_space - root_size
    required_space = update_size - unused
    # get a list of directories with enough space and sort them in ascending order
    suitable_dirs = sorted(list(filter(lambda x: x[1] >= required_space, dir_list)), key=lambda y: y[1])
    best_choice = suitable_dirs[0]
    size_of_choice = best_choice[1]
    return p1answer, size_of_choice


if __name__ == '__main__':
    FILENAME = './input/day7.txt'
    with open(FILENAME) as f:
        s = f.read().strip().split('\n')

    print(main(s, 70000000, 30000000))
