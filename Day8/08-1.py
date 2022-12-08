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

def visible_sides(trees: list, row_index: int, col_index: int) -> int:
    sides_found = 0
    tree_height = trees[row_index][col_index]
    row = trees[row_index]
    col = [tree[col_index] for tree in trees]

    # Check left
    section = row[:col_index + 1]
    if is_visible(section, tree_height): sides_found += 1

    # Check right
    section = row[col_index:]
    if is_visible(section, tree_height): sides_found += 1

    # Check top
    section = col[:row_index + 1]
    if is_visible(section, tree_height): sides_found += 1

    # Check bottom
    section = col[row_index:]
    if is_visible(section, tree_height): sides_found += 1

    return sides_found

def is_visible(section: list, tree_height: int):
    return (max(section) == tree_height and section.count(tree_height) == 1)

def problem1(trees: list) -> int:
    visible_found = 0
    # Row index and row value
    for row_index, row_value in enumerate(trees):
        # Column index and column value
        for col_index, col_value in enumerate(trees):
            if visible_sides(trees, row_index, col_index) > 0:
                visible_found += 1

    return visible_found

trees = handle_input()
print(f'Total: {problem1(trees)}')