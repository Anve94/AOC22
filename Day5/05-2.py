from collections import deque
from os import path
import re

global STACKS
STACKS = []

def start_configuration() -> list:
    global STACKS
    STACKS = [deque('WDGBHRV'), deque('JNGCRF'), deque('LSFHDNJ'), deque('JDSV'), deque('SHDRQWNV'), deque('PGHCM'), deque('FJBGLZHC'), deque('SJR'), deque('LGSRBNVM')]

def handle_input():
    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, 'in.txt')
    with open(filename, 'r') as f:
        for line in f:
            operation = line.rstrip('\n')
            found = parse_line(operation)
            update_stack(found)

def parse_line(line: str) -> tuple:
    found = re.findall('\d+', line)
    return (int(found[0]), int(found[1]), int(found[2]))

def update_stack(operations: tuple) -> None:
    global STACKS
    (amount, from_pos, to_pos) = operations
    to_update = [STACKS[from_pos - 1].pop() for _ in range(0, amount)]
    to_update.reverse()
    _ = [STACKS[to_pos - 1].append(value) for value in to_update]

start_configuration()
handle_input()
solution = ''
for s in STACKS:
    solution += s.pop()

print(solution)