totals = []
total = 0
top_limit = 3
with open('01-1.txt', 'r') as f:
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