import sys
import re

from functools import reduce


with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip,f.readlines()))

times = map(int,re.findall(r'\d+', lines[0]))
distances = map(int,re.findall(r'\d+', lines[1]))

pairs = zip(times, distances)

def count_record_beaters(pair):
    time, max_d = pair
    count = 0
    for t in range(time):
        if t * (time-t) > max_d:
            count += 1

    return count

# Part 1
print(reduce(lambda a, c: a*c, map(count_record_beaters, pairs), 1))

time = int(''.join(re.findall(r'\d+', lines[0])))
distance = int(''.join(re.findall(r'\d+', lines[1])))

# Part 2
print(count_record_beaters((time, distance)))
