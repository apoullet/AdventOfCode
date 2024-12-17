import sys
from functools import cmp_to_key


with open(sys.argv[1], 'r') as p_input:
    [rules, updates] = p_input.read().strip().split('\n\n')

    rules   = rules.split('\n')
    updates = updates.split('\n')

smaller_than = {}

for rule in rules:
    [left, right] = rule.split('|')
    smaller_than[right] = {*smaller_than.get(right, []), left}

def compare(i1, i2):
    if i1 in smaller_than[i2]:
        return -1
    elif i2 in smaller_than[i1]:
        return 1
    else:
        return 0

total  = 0
total2 = 0
for update_str in updates:
    update = update_str.split(',')
    if update == sorted(update,key=cmp_to_key(compare)):
        middle_number = int(update[len(update)//2])
        total += middle_number
    else:
        middle_number = int(sorted(update,key=cmp_to_key(compare))[len(update)//2])
        total2 += middle_number

print(total, total2)