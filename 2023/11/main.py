import sys

from dataclasses import dataclass
from functools import partial


@dataclass()
class Galaxy:
    pos: tuple[int, int]
    index: int

def get_lines(offset=1):
    lines = []
    offset_str = str(offset)
    for line in map(str.strip,open(sys.argv[1]).readlines()):
        lines.append([line[0]])
        for char in line[1:]:
            lines[-1].append(char)

    for y in range(len(lines)):
        if '#' not in lines[y]:
            for x in range(len(lines[y])):
                lines[y][x] = offset_str

    for x in range(len(lines[0])):
        found = False
        for y in range(len(lines)):
            if lines[y][x] == '#':
                found = True

        if not found:
            for y in range(len(lines)):
                lines[y][x] = offset_str
    return lines

def get_galaxies(lines):
    galaxies = []
    count = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == '#':
                galaxies.append(Galaxy((x, y), count))
                count += 1
    return galaxies

def get_pairs(galaxies):
    for g1 in galaxies:
        for g2 in galaxies[1:]:
            if g1 != g2 and g1.index < g2.index:
                yield (g1.pos, g2.pos)

def manhattan_inner(lines, pos):
    x1, y1 = pos[0]
    x2, y2 = pos[1]
    offset = 0

    ycopy, yoffset = y1, 1 if y1 < y2 else -1
    while ycopy != y2:
        ycopy += yoffset
        if lines[ycopy][x1] != '.' and lines[ycopy][x1] != '#':
            offset += int(lines[ycopy][x1])

    xcopy, xoffset = x1, 1 if x1 < x2 else -1
    while xcopy != x2:
        xcopy += xoffset
        if lines[y1][xcopy] != '.' and lines[y1][xcopy] != '#':
            offset += int(lines[y1][xcopy])

    return abs(x1-x2) + abs(y1-y2) + offset

lines = get_lines()
manhattan = partial(manhattan_inner, lines)

galaxies = get_galaxies(lines)

distances = map(manhattan, get_pairs(galaxies))

print(sum(distances))

lines2 = get_lines(999_999)
manhattan2 = partial(manhattan_inner, lines2)

distances2 = map(manhattan2, get_pairs(galaxies))

print(sum(distances2))
