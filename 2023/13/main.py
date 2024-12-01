import sys


mirrors = [mirror.split('\n') for mirror in map(str.strip,open(sys.argv[1]).read().split('\n\n'))]

def is_reflection(start_idx, mirror, is_ver):
    if is_ver:
        if start_idx == 1:
            return True
        
        current = start_idx
        reflect = start_idx-1

        while current < len(mirror) and reflect >= 0:
            if mirror[current] != mirror[reflect]:
                return False
            current += 1
            reflect -= 1
        return True
    else:
        if start_idx == 1:
            return True
        
        current = start_idx
        reflect = start_idx-1

        while current < len(mirror[0]) and reflect >= 0:
            current_col = ''.join([mirror[y][current] for y in range(len(mirror))])
            reflect_col = ''.join([mirror[y][reflect] for y in range(len(mirror))])
            if current_col != reflect_col:
                return False
            current += 1
            reflect -= 1
        return True

def get_reflection_value(mirror):
    seen_ver = set()
    for y in range(len(mirror)):
        if mirror[y] in seen_ver:
            print("Seen ver:", mirror[y], y)
            if is_reflection(y, mirror, True):
                    return y * 100
        seen_ver.add(mirror[y])

    seen_hor = set()
    for x in range(len(mirror[0])):
        col = ''.join([mirror[y][x] for y in range(len(mirror))])
        if col in seen_hor:
            print("Seen hor:", col, x)
            if is_reflection(x, mirror, False):
                    return x
        seen_hor.add(col)
    return 0

total = 0
for mirror in mirrors:
    print()
    value = get_reflection_value(mirror)
    total += value

print(total)

def find_diffs(line1, line2):
    diffs = []
    for i, (c1, c2) in enumerate(zip(line1, line2)):
        if c1 != c2:
            diffs.append(i)
    return diffs

def get_fixed_smudge_reflection_value(mirror):
    first_row = mirror[0]
    for y in range(1, len(mirror)):
        diffs = find_diffs(first_row, mirror[y])

        if len(diffs) == 1:
            print('found fr smudge at', y)
            return (y + 1) / 2 * 100
    last_row = mirror[-1]
    for y in range(len(mirror[1:])-2, -1, -1):
        diffs = find_diffs(last_row, mirror[y])

        if len(diffs) == 1:
            print('found lr smudge at', y)
            return (len(mirror)-y) / 2 * 100

    first_col = ''.join([mirror[y][0] for y in range(len(mirror))])
    for x in range(1, len(mirror[0])):
        current_col = ''.join([mirror[y][x] for y in range(len(mirror))])
        diffs = find_diffs(first_col, current_col)

        if len(diffs) == 1:
            print('found fc smudge at', x)
            return (x + 1) / 2
    last_col = ''.join([mirror[y][-1] for y in range(len(mirror))])
    for x in range(len(mirror[0][1:])-2, -1, -1):
        current_col = ''.join([mirror[y][x] for y in range(len(mirror))])
        diffs = find_diffs(last_col, current_col)

        if len(diffs) == 1:
            print('found lc smudge at', x)
            return (len(mirror[0])-x) / 2

    return 0

total = 0
for mirror in mirrors:
    value = get_fixed_smudge_reflection_value(mirror)
    print(value)
    total += value

print(total)

