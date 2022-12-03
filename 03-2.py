LOWER_CASE_OFFSET = 96 # Offset from ASCII to ensure a starts at 1
UPPER_CASE_OFFSET = 38 # Offset from ASCII to ensure A starts at 27

def input_to_backpacks() -> list:
    backpacks = []
    with open('03-1.txt', 'r') as f:
        for line in f:
            backpack = line.rstrip('\n')
            backpacks.append(backpack)
            
    return backpacks

def items_to_priority(items: list) -> int:
    score = 0
    for item in items:
        score += get_priority_for_item(item)
    
    return score

def get_priority_for_item(item: str) -> int:
    if item.isupper():
        return ord(item) - UPPER_CASE_OFFSET
    
    return ord(item) - LOWER_CASE_OFFSET

def get_groups(backpacks: list) -> list:
    i = 0
    groups = []
    group = []
    for backpack in backpacks:        
        group.append(backpack)
        i += 1
        
        if i % 3 == 0:
            groups.append(group)
            group = []
            i = 0
        
    return groups

def check_groups(groups: list) -> list:
    found = []
    for group in groups:
        found += list(
            set(group[0]).intersection(group[1], group[2])
        )
        
    return found
            
        
backpacks = input_to_backpacks()
groups = get_groups(backpacks)
print(groups)
found = check_groups(groups)
print(items_to_priority(found))