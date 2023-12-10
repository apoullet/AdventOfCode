import sys

from dataclasses import dataclass


@dataclass(frozen=True)
class Tile:
    pos: tuple[int, int]
    value: str

    def get_adjacent_tiles(self, tiles, width):
        x, y = self.pos

        offset = y * width

        north = tiles[x + offset - width]
        east  = tiles[x + 1 + offset]
        south = tiles[x + offset + width]
        west  = tiles[x - 1 + offset]

        return [north, east, south, west]

lines = list(map(str.strip,open(sys.argv[1]).readlines()))


lines.insert(0,'.'*len(lines[0]))
lines.insert(len(lines),'.'*len(lines[0]))

for i in range(len(lines)):
    lines[i] = f".{lines[i]}."

GRID_WIDTH = len(lines[0])
GRID_HEIGHT = len(lines)

tiles = [Tile((x, y), lines[y][x]) for y in range(GRID_HEIGHT) for x in range(GRID_WIDTH)]

dir2symbol = {
    'N': ['|', '7', 'F', 'S'],
    'E': ['-', 'J', '7', 'S'],
    'S': ['|', 'L', 'J', 'S'],
    'W': ['-', 'L', 'F', 'S'],
}

symbol2dir = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    'L': ['N', 'E'],
    'J': ['N', 'W'],
    '7': ['S', 'W'],
    'F': ['S', 'E']
}

s_idx = list(map(lambda t: t.value, tiles)).index('S')
s = tiles[s_idx]

def get_tube_loop(s_tile, tiles, width):
    loop = [s_tile]

    n, e, s, w = s_tile.get_adjacent_tiles(tiles, width)

    if n.value in dir2symbol['N']:
        loop.append(n)
    elif e.value in dir2symbol['E']:
        loop.append(e)
    elif s.value in dir2symbol['S']:
        loop.append(s)
    else:
        loop.append(w)

    previous = s_tile
    current = loop[-1]

    while (next:=get_next_tile(current, previous, tiles, width)) != s_tile:
        loop.append(next)

        previous, current = current, next

    return loop

def get_next_tile(current, previous, tiles, width):
    directions = symbol2dir[current.value]
    n, e, s, w = current.get_adjacent_tiles(tiles, width)

    for direction in directions:
        if direction == 'N':
            if n != previous:
                return n
        if direction == 'E':
            if e != previous:
                return e
        if direction == 'S':
            if s != previous:
                return s
        if direction == 'W':
            if w != previous:
                return w
    return None

loop = get_tube_loop(s, tiles, GRID_WIDTH)
print(len(loop) // 2)

def get_maybe_enclosed_tiles(tiles, loop, width, height):
    for y in range(0, height):
        offset = y * width
        for x in range(0, width):
            tile = tiles[x + offset]
            if tile not in loop:
                yield tile

def get_enclosed_tiles(tiles, loop, width, height):
    enclosed_count = 0
    for tile in get_maybe_enclosed_tiles(tiles, loop, width, height):
        hor_idx = get_hor_bounds(tile, loop)
        ver_idx = get_ver_bounds(tile, loop)

        if hor_idx % 2 == 0 and ver_idx % 2 == 0:
            enclosed_count += 1

    return enclosed_count

def get_hor_bounds(tile, loop):
    _, y = tile.pos

    bounds = []
    bound_tiles = [lt for lt in loop if lt.pos[1] == y and lt.value != '-' and lt.value != 'S']
    bound_tiles.sort(key=lambda t: t.pos[0])

    for loop_tile in bound_tiles:
        if len(bounds) == 0:
            bounds.append(loop_tile)
        else:
            if bounds[-1].value + loop_tile.value not in ['FJ','L7']:
                bounds.append(loop_tile)
    bounds.append(tile)
    bounds.sort(key=lambda t: t.pos[0])

    return bounds.index(tile) + 1

def get_ver_bounds(tile, loop):
    x, _ = tile.pos

    bounds = []
    bound_tiles = [lt for lt in loop if lt.pos[0] == x and lt.value != '|' and lt.value != 'S'];
    bound_tiles.sort(key=lambda t: t.pos[1])
     
    for loop_tile in bound_tiles:
        if len(bounds) == 0:
            bounds.append(loop_tile)
        else:
            if bounds[-1].value + loop_tile.value not in ['FJ', '7L']:
                bounds.append(loop_tile)
    bounds.append(tile)
    bounds.sort(key=lambda t: t.pos[1])

    return bounds.index(tile) + 1

print(get_enclosed_tiles(tiles, loop, GRID_WIDTH, GRID_HEIGHT))
