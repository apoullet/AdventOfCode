import sys
import re


lines = list(map(str.strip,open(sys.argv[1]).readlines()))

def is_valid(current, backup):
    return all(map(lambda p: p[0] == p[1], zip(current,backup)))

def a2t(arrangement, qm_index):
    splita = arrangement[:qm_index].split('.')[:-1]
    return filter(None,map(len, splita))

def is_possible(arrangement, qm_index, joined_groups):
    last_group_complete = arrangement[qm_index-1] == '.'
    splita = list(filter(None,arrangement[:qm_index].split('.')))

    if '#' not in arrangement[:qm_index]:
        return True
    if len(splita) > len(joined_groups):
        return False
    if joined_groups[len(splita)-1] < len(splita[-1]):
        return False
    if last_group_complete and joined_groups[len(splita)-1] != len(splita[-1]):
        return False
    if not all(map(lambda p: p[0] == p[1], zip(map(len, splita[:-1]), joined_groups))):
        return False
    return True
sc = 0

def get_arrangements_count_re(record, joined_groups, memo):
    # print(record, memo)
    global sc
    sc += 1
    if '?' not in record:
        # print(record, tuple(filter(None,map(len,record.split('.')))) == joined_groups)
        return int(tuple(filter(None,map(len,record.split('.')))) == joined_groups)
    qm_index = record.index('?')

    if not is_possible(record, qm_index, joined_groups):
        # print("Not possible:", record, False)
        return 0

    key = f"{qm_index}-{record[qm_index-1]}-{tuple(map(len,filter(None,record[:qm_index].split('.'))))}"

    if key in memo:
        # print(key, record, memo[key])
        return memo[key]
    
    count = get_arrangements_count_re(record.replace('?', '#', 1), joined_groups, memo) + get_arrangements_count_re(record.replace('?', '.', 1), joined_groups, memo)
    # print(record, count)
    memo[key] = count
    return count

total = 0
for line in lines:
    record, backup = line.split(' ')

    unfolded_record = '?'.join([record] * 5)
    unfolded_backup = ','.join([backup] * 5)
    # print(record, backup)
    joined_groups = tuple(map(int, unfolded_backup.split(',')))
    memo = {}
    count = get_arrangements_count_re(unfolded_record, joined_groups, memo)
    # print(sc, count)
    sc = 0
    total += count 
print(total)
