import collections
from os import path

def handle_input():
    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, 'in.txt')
    found = []
    with open(filename, 'r') as f:
        for lines in f.readlines():
            command_part = lines.rstrip().split(' ')
            found.append(command_part)
    return found


def create_fs(user_input: list) -> dict:
    fs = dict()
    dir_stack = collections.deque() # A stack is just a lazy man's recursion anyway

    for command_part in user_input:
        if command_part[0] == '$' and command_part[1] == 'cd':
            # Handle going back to root by clearing the stack
            if command_part[2] == '/':
                dir_stack.clear()
                dir_stack.append('/')

            elif command_part[2] == '..':
                # Sanity check for root dir
                if dir_stack[-1] != '/':
                    dir_stack.pop()
            else:
                dir_stack.append(command_part[2])

        elif command_part[0][0].isdigit():
            cur_path = fs
            for i, value in enumerate(dir_stack):
                if value not in cur_path:
                    cur_path[value] = {'dir': dict(), 'files': [0]}

                if i == len(dir_stack) - 1:
                    cur_path = cur_path[value]

                else:
                    cur_path = cur_path[value]['dir']

            cur_path['files'].append(int(command_part[0]))

    return fs

def recursive_walk(folder, current_path, folder_sizes, max_size):
    folder_size = sum(folder['files'])
    if len(folder['dir']) == 0:
        folder_sizes["/".join(current_path)] = folder_size
        return folder_size, folder_size if folder_size <= max_size else 0

    smaller_cumalative = 0
    for name, dir in folder['dir'].items():
        current_path.append(name)
        dir_space, dir_smaller = recursive_walk(dir, current_path, folder_sizes, max_size)
        current_path.pop()
        folder_size += dir_space
        smaller_cumalative += dir_smaller

    folder_sizes["/".join(current_path)] = folder_size
    return folder_size, smaller_cumalative + folder_size if folder_size <= max_size else smaller_cumalative


def problem1():
    user_input = handle_input()
    fs = create_fs(user_input)

    folder_sizes = dict()
    current_path = collections.deque(['/'])
    disk_room, smaller_cumalative = recursive_walk(fs['/'], current_path, folder_sizes, 100_000)
    print(smaller_cumalative)


def problem2():
    user_input = handle_input()
    fs = create_fs(user_input)

    folder_sizes = dict()
    current_path = collections.deque(['/'])
    disk_room, smaller_cumalative = recursive_walk(fs['/'], current_path, folder_sizes, 100_000)

    need_to_free = 30_000_000 - (70_000_000 - disk_room)

    # go through the sizes and find the smallest one larger than the space we need to free
    min_space = 70_000_000
    for value in folder_sizes.values():
        if value > need_to_free:
            min_space = min(min_space, value)

    print(min_space)

problem1()
problem2()