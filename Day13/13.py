# See: https://docs.python.org/3/library/functools.html#functools.cmp_to_key
from functools import cmp_to_key
from math import prod
from os import path

def compare(left, right):
    """
    Compare left and right values.
    Inspiration from https://peps.python.org/pep-0622/
    """
    match left, right:
        case int(), list():
            # Compare left as list if only right is list
            return compare([left], right)
        case list(), int():
            # Compare right as list if only left is list
            return compare(left, [right])
        case list(), list():
            # Iterate over list recursively
            for x in map(compare, left, right):
                if x:
                    return x
            return compare(len(left), len(right))
        case int(), int():
            # If both values are integers, the lower integer should come first.
            # If the left integer is lower than the right integer, the inputs are in the right order.
            # Evaluates to 1 if left > right, 0 if left == right and -1 if right > 1
            return (left > right) - (left < right)

def handle_input():
    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, 'in.txt')
    comparisons = []
    with open (filename) as f:
        lines = f.read().split('\n\n')
    for line in lines:
        comparisons.append([*map(eval, line.split())])
    return comparisons

def problem_1(comparisons):
    indexes_found = []
    for index, comparison in enumerate(comparisons, start = 1):
        comparison_result = compare(*comparison)
        if comparison_result == -1:
            indexes_found.append(index)

    print(f'Solution to part 1: {sum(indexes_found)}')

def problem_2(comparisons):
    sorted_key = cmp_to_key(compare)
    # Since we convert our compare function to a modern key, we can also sort it based on the sum of compare results
    comparisons = sorted(sum(comparisons, [[2], [6]]), key=sorted_key)
    indexes_found = [index for index, comparison in enumerate(comparisons, start=1) if comparison in ([2], [6])]
    print(f'Solution to part 2: {prod(indexes_found)}')

comparisons = handle_input()
problem_1(comparisons)
problem_2(comparisons)

