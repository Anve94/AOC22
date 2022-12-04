from os import path

LOWER_CASE_OFFSET = 96 # Offset from ASCII to ensure a starts at 1
UPPER_CASE_OFFSET = 38 # Offset from ASCII to ensure A starts at 27

def input_to_backpacks() -> list:
    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, '03-1.txt')
    backpacks = []
    
    with open(filename, 'r') as f:
        for line in f:
            found = line.rstrip('\n')
            size = len(found) // 2
            left = found[:size]
            right = found[size:]
            backpack = [left, right]
            backpacks.append(backpack)
            
    return backpacks

def find_duplicated(backpacks: list) -> list:
    duplicated_items = []
    for backpack in backpacks:
        duplicated_items += next((i for i in backpack[0] if i in backpack[1]), None)
        
    return duplicated_items

def items_to_priority(items: list) -> int:
    score = 0
    for item in items:
        score += get_priority_for_item(item)
    
    return score

def get_priority_for_item(item: str) -> int:
    if item.isupper():
        return ord(item) - UPPER_CASE_OFFSET
    
    return ord(item) - LOWER_CASE_OFFSET
        

backpacks = input_to_backpacks()
dupes = find_duplicated(backpacks)
print(items_to_priority(dupes))
