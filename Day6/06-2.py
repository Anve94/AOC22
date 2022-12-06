from os import path

def handle_input():
    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, 'in.txt')
    with open(filename, 'r') as f:
        found = f.readline()
        return find_non_repeating(found)

def find_non_repeating(message: str) -> int:
    found = False
    left_limit = 0
    right_limit = 14

    while found == False:
        current_set = message[left_limit:right_limit]
        if not has_repeating(current_set):
            found = True
        else:
            left_limit += 1
            right_limit += 1

    return right_limit

def has_repeating(part: str) -> bool:
    return len(set(part)) != len(part)

solution = handle_input()
print(solution)