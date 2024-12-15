import sys


with open(sys.argv[1], 'r') as p_input:
    lines = list(map(str.strip, p_input.readlines()))

total = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 'X':
            # horizontal
            if x < len(lines[0])-3 and lines[y][x+1] == 'M' and lines[y][x+2] == 'A' and lines[y][x+3] == 'S':
                total += 1
            if x > 2 and lines[y][x-1] == 'M' and lines[y][x-2] == 'A' and lines[y][x-3] == 'S':
                total += 1
            # vertical
            if y < len(lines)-3 and lines[y+1][x] == 'M' and lines[y+2][x] == 'A' and lines[y+3][x] == 'S':
                total += 1
            if y > 2 and lines[y-1][x] == 'M' and lines[y-2][x] == 'A' and lines[y-3][x] == 'S':
                total += 1
            # diagonal
            if x < len(lines[0])-3 and y > 2 and lines[y-1][x+1] == 'M' and lines[y-2][x+2] == 'A' and lines[y-3][x+3] == 'S':
                total += 1
            if x < len(lines[0])-3 and y < len(lines)-3 and lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S':
                total += 1
            if x > 2 and y < len(lines)-3 and lines[y+1][x-1] == 'M' and lines[y+2][x-2] == 'A' and lines[y+3][x-3] == 'S':
                total += 1
            if x > 2 and y > 2 and lines[y-1][x-1] == 'M' and lines[y-2][x-2] == 'A' and lines[y-3][x-3] == 'S':
                total += 1

print(total)

total = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 'A':
            if y > 0 and x > 0 and y < len(lines)-1 and x < len(lines[0])-1:
                if lines[y-1][x-1] == 'M':
                    if lines[y+1][x+1] != 'S':
                        continue
                    if lines[y-1][x+1] == 'M':
                        if lines[y+1][x-1] != 'S':
                            continue
                    elif lines[y-1][x+1] == 'S':
                        if lines[y+1][x-1] != 'M':
                            continue
                    else:
                        continue
                elif lines[y-1][x-1] == 'S':
                    if lines[y+1][x+1] != 'M':
                        continue
                    if lines[y-1][x+1] == 'M':
                        if lines[y+1][x-1] != 'S':
                            continue
                    elif lines[y-1][x+1] == 'S':
                        if lines[y+1][x-1] != 'M':
                            continue
                    else:
                        continue
                else:
                    continue

                total += 1;

print(total)