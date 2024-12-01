import sys

from copy import deepcopy


lines = [[c for c in line] for line in map(str.strip,open(sys.argv[1], 'r').readlines())]

def tilt_north(lines):
    for y in range(1, len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] != 'O':
                continue
            current_y = y-1

            while current_y > 0 and lines[current_y][x] == '.':
                current_y -= 1

            if current_y == 0 and lines[current_y][x] == '.':
                lines[current_y][x] = 'O'
                lines[y][x]         = '.'
            elif current_y != y-1:
                lines[current_y+1][x] = 'O'
                lines[y][x]         = '.'

total = 0
lcopy = deepcopy(lines)
tilt_north(lcopy)
for y in range(len(lcopy)):
    for x in range(len(lcopy[0])):
        if lcopy[y][x] == 'O':
            total += (len(lcopy)-y)
print(total)

def tilt_west(lines):
    for x in range(1, len(lines[0])):
        for y in range(len(lines)):
            if lines[y][x] != 'O':
                continue
            current_x = x-1

            while current_x > 0 and lines[y][current_x] == '.':
                    current_x -= 1

            if current_x == 0 and lines[y][current_x] == '.':
                lines[y][current_x] = 'O'
                lines[y][x]         = '.'
            elif current_x != x-1:
                lines[y][current_x+1] = 'O'
                lines[y][x]           = '.'

def tilt_south(lines):
    for y in range(len(lines)-2,-1,-1):
        for x in range(len(lines[0])):
            if lines[y][x] != 'O':
                continue
            current_y = y+1

            while current_y < len(lines)-1 and lines[current_y][x] == '.':
                current_y += 1

            if current_y == len(lines)-1 and lines[current_y][x] == '.':
                lines[current_y][x] = 'O'
                lines[y][x]         = '.'
            elif current_y != y+1:
                lines[current_y-1][x] = 'O'
                lines[y][x]         = '.'

def tilt_east(lines):
    for x in range(len(lines[0])-2, -1, -1):
        for y in range(len(lines)):
            if lines[y][x] != 'O':
                continue
            current_x = x+1

            while current_x < len(lines[0])-1 and lines[y][current_x] == '.':
                    current_x += 1

            if current_x == len(lines[0])-1 and lines[y][current_x] == '.':
                lines[y][current_x] = 'O'
                lines[y][x]         = '.'
            elif current_x != x+1:
                lines[y][current_x-1] = 'O'
                lines[y][x]           = '.'

def cycle(lines):
    tilt_north(lines)
    tilt_west(lines)
    tilt_south(lines)
    tilt_east(lines)

cycles = []
total_cycles = 0
current = deepcopy(lines)
while True:
    cycle(current)
    total_cycles += 1
    if current in cycles:
        break
    else:
        cycles.append(deepcopy(current))

current_idx = cycles.index(current)
cycle_count = (1_000_000_000 - current_idx) % (total_cycles - (current_idx + 1))

for _ in range(current_idx + cycle_count):
    cycle(lines)

total2 = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 'O':
            total2 += (len(lines)-y)
print(total2)
