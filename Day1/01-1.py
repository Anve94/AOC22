from os import path

totals = []
total = 0
top_limit = 3

here = path.dirname(path.abspath(__file__))
filename = path.join(here, '01-1.txt')
    
with open(filename, 'r') as f:
    for line in f:
        found = line.strip('\n')
        if found == '':
            totals.append(total)
            total = 0
        else:
            total += int(found)
    
print(f'Best prepared elf is carrying {max(totals)} calories')
      
top_elves = []
for i in range(0, top_limit):
    highest = max(totals)
    top_elves.append(highest)
    totals.remove(highest)
    
print(f'The top {top_limit} elves are carrying {sum(top_elves)} calories')