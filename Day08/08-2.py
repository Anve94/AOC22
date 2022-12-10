from os import path

def handle_input() -> list:
    """Represent input file as 2d list"""

    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, 'in.txt')
    trees = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            trees.append([int(c) for c in line])

    return trees

def viewing_distance(trees: list, row_index: int, col_index: int) -> int:
    viewing_distance = 1 # Default to 1 since x * 1 is still x
    tree_height = trees[row_index][col_index]
    row = trees[row_index]
    col = [tree[col_index] for tree in trees]

    # Check left
    section = row[:col_index + 1]
    section.reverse()
    # Since the slice is left to right, we reverse the list and look for the first
    # tree that is equal or heigher to the current tree. It's position in the slice relates
    # to the viewing distance. If no such tree is found, we can see all the trees up to the edge
    # of the forest, and can simply use the length of the sliced list to determine the distance to
    # the edge of the forest.
    viewing_distance *= get_distance(section, tree_height)

    # Check right
    section = row[col_index:]
    viewing_distance *= get_distance(section, tree_height)

    # Check top
    section = col[:row_index + 1]
    section.reverse()
    viewing_distance *= get_distance(section, tree_height)

    # Check bottom
    section = col[row_index:]
    viewing_distance *= get_distance(section, tree_height)

    return viewing_distance

def get_distance(section: list, tree_height: int) -> int:
    # Since the slice contains the tree we're tracking for, we remove it here for these checks
    for k, v in enumerate(section[1:]):
        if v >= tree_height:
            return k + 1
        
    if len(section) > 1: return len(section[1:])
    return 1

def problem2(trees: list) -> int:
    distances = []
    for row_index, row_value in enumerate(trees):
        for col_index, col_value in enumerate(trees):
            distances.append(viewing_distance(trees, row_index, col_index))

    return max(distances)

trees = handle_input()
print(f'Total: {problem2(trees)}')