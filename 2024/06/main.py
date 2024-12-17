import sys


with open(sys.argv[1], 'r') as p_input:
    lines = list(map(str.strip,p_input.readlines()))

def get_start(lines):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == '^':
                return y, x

cury, curx = get_start(lines)
# 0 - up
# 1 - right
# 2 - down
# 3 - left
direction = 0

visited_pos = set()
while True:
    if direction == 0:
        if cury-1 == -1:
            visited_pos.add((cury,curx))
            break
        if lines[cury-1][curx] == '#':
            direction = 1
        else:
            visited_pos.add((cury,curx))
            cury -= 1
    elif direction == 1:
        if curx+1 == len(lines[0]):
            visited_pos.add((cury,curx))
            break
        if lines[cury][curx+1] == '#':
            direction = 2
        else:
            visited_pos.add((cury,curx))
            curx += 1
    elif direction == 2:
        if cury+1 == len(lines):
            visited_pos.add((cury,curx))
            break
        if lines[cury+1][curx] == '#':
            direction = 3
        else:
            visited_pos.add((cury,curx))
            cury += 1
    elif direction == 3:
        if curx-1 == -1:
            visited_pos.add((cury,curx))
            break
        if lines[cury][curx-1] == '#':
            direction = 0
        else:
            visited_pos.add((cury,curx))
            curx -= 1

print(len(visited_pos))

loop_count = 0
for pos in visited_pos:
    lines_cp = list(lines)
    lines_cp[pos[0]] = lines_cp[pos[0]][:pos[1]] + '#' + lines_cp[pos[0]][pos[1]+1:]
    cury, curx = get_start(lines)
    obstacles_hit = set()
    direction = 0
    while True:
        if direction == 0:
            if cury-1 == -1:
                break
            if lines_cp[cury-1][curx] == '#':
                if (cury-1,curx,direction) in obstacles_hit:
                    loop_count += 1
                    break
                obstacles_hit.add((cury-1,curx,direction))
                direction = 1
            else:
                cury -= 1
        elif direction == 1:
            if curx+1 == len(lines_cp[0]):
                break
            if lines_cp[cury][curx+1] == '#':
                if (cury,curx+1,direction) in obstacles_hit:
                    loop_count += 1
                    break
                obstacles_hit.add((cury,curx+1,direction))
                direction = 2
            else:
                curx += 1
        elif direction == 2:
            if cury+1 == len(lines_cp):
                break
            if lines_cp[cury+1][curx] == '#':
                if (cury+1,curx,direction) in obstacles_hit:
                    loop_count += 1
                    break
                obstacles_hit.add((cury+1,curx,direction))
                direction = 3
            else:
                cury += 1
        elif direction == 3:
            if curx-1 == -1:
                break
            if lines_cp[cury][curx-1] == '#':
                if (cury,curx-1,direction) in obstacles_hit:
                    loop_count += 1
                    break
                obstacles_hit.add((cury,curx-1,direction))
                direction = 0
            else:
                curx -= 1

print(loop_count)