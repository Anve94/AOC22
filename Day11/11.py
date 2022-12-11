from collections import deque
from os import path
import re

# Thanks project euler
def get_divisble_product(test_conditions: list):
    found = 1
    for x in test_conditions:
        found = found * x
        
    return found
    
def problem_1():
    monkeys = [0 for monkey in range(len(test_conditions))] # Init items monkeys checked to 0
    # Represent items as queue so we can pop left more easily to get first item in list
    items = [deque(x for x in line2numbers.findall(lines[y])) for y in range(1, len(lines), 7)]
    
    for _round in range(0, 20):
        for monkey in range(0, len(monkeys)):
            while len(items[monkey]) > 0:
                worry_level = int(items[monkey].popleft())
                
                if operations[monkey].find("old") > -1:
                    worry_level *= worry_level
                    
                elif operations[monkey].find("+ ") > -1:
                    worry_level += int(line2numbers.findall(operations[monkey])[0])
                    
                elif operations[monkey].find("* ") > -1:
                    worry_level *= int(line2numbers.findall(operations[monkey])[0])
                    
                worry_level = worry_level // 3
                
                if worry_level % test_conditions[monkey] == 0:
                    items[tests_outcome_mapping[monkey][0]].append(worry_level)
                    
                else:
                    items[tests_outcome_mapping[monkey][1]].append(worry_level)
                monkeys[monkey] += 1
                
    answer = sorted(monkeys)
    return answer[-1] * answer[-2]

def problem_2():
    monkeys = [0 for monkey in range(len(test_conditions))] # Init items monkeys checked to 0
    # Represent items as queue so we can pop left more easily/verbosely to get first item in list
    items = [deque(x for x in line2numbers.findall(lines[y])) for y in range(1, len(lines), 7)]
    common_divider = get_divisble_product(test_conditions)
    
    for _round in range(0, 10000):
        for monkey in range(0, len(monkeys)):
            while len(items[monkey]) > 0:
                worry_level = int(items[monkey].popleft())
                
                if operations[monkey].find("old") > -1:
                    worry_level *= worry_level
                    
                elif operations[monkey].find("+ ") > -1:
                    worry_level += int(line2numbers.findall(operations[monkey])[0])
                    
                elif operations[monkey].find("* ") > -1:
                    worry_level *= int(line2numbers.findall(operations[monkey])[0])
                    
                worry_level = worry_level % common_divider
                
                if worry_level % test_conditions[monkey] == 0:
                    items[tests_outcome_mapping[monkey][0]].append(worry_level)
                    
                else:
                    items[tests_outcome_mapping[monkey][1]].append(worry_level)
                monkeys[monkey] += 1
                
    answer = sorted(monkeys)
    return answer[-1] * answer[-2]

def handle_input() -> list:
    here = path.dirname(path.abspath(__file__))
    filepath = path.join(here, "in.txt")

    with open(filepath, "r") as f:
        lines = f.read().splitlines()
        
    return lines

lines = handle_input()
line2numbers = re.compile(r'\d+')

# Start on line 2, get 23rd character onwards and every 7th line after
# We need characters too so this seems the easiest way to get the sign, "old" and digit/value
operations = [(lines[x][23:]) for x in range(2, len(lines), 7)]
print(operations)

# Get conditions from line 3 and every 7th line thereafter
test_conditions = [line2numbers.findall(lines[x])[0] for x in range(3, len(lines), 7)]
test_conditions = [int(x) for x in test_conditions]
print(test_conditions)

# Get true/false conditions
tests_outcome_mapping = []
trues = [line2numbers.findall(lines[x])[0] for x in range(4, len(lines), 7)]
falses = [line2numbers.findall(lines[x])[0] for x in range(5, len(lines), 7)]
print(trues)
for i in range(0, len(trues)):
    tests_outcome_mapping += [
        [
            int(trues[i]),
            int(falses[i])
        ]
    ]
    
print(tests_outcome_mapping)

print(f'Part 1: {problem_1()}')
print(f'Part 2: {problem_2()}')