with open('input.txt', 'r') as f:
    lines = list(map(str.strip,f.readlines()))

lines.insert(0,'.'*len(lines[0]))
lines.insert(len(lines),'.'*len(lines[0]))

for i in range(len(lines)):
    lines[i] = f".{lines[i]}."

## [[ Part 1 ]] ##

def issymbol(character):
    return character != '.' and not character.isdigit()

def get_indices_around_symbol(x, y):
    return [
        (x-1,y-1),
        (x,y-1),
        (x+1,y-1),
        (x-1,y),
        (x+1,y),
        (x-1,y+1),
        (x,y+1),
        (x+1,y+1),
    ]

def get_number_at_index(x, y, lines):
    if (lines[y][x] == '.'):
        return 0

    number_string = lines[y][x]

    i = 1
    while lines[y][x-i].isdigit():
        number_string = f"{lines[y][x-i]}{number_string}"
        lines[y] = f"{lines[y][:x-i]}.{lines[y][x-i+1:]}"
        i +=1

    j = 1
    while lines[y][x+j].isdigit():
        number_string = f"{number_string}{lines[y][x+j]}"
        lines[y] = f"{lines[y][:x+j]}.{lines[y][x+j+1:]}"
        j += 1

    return int(number_string)


part1 = 0
lines1 = list(lines)

for x in range(len(lines[0])-2):
    for y in range(len(lines)-2):
        if issymbol(lines[y][x]):
            indices = get_indices_around_symbol(x,y)

            for xx, yy in indices:
                part1 += get_number_at_index(xx,yy,lines1)


print(part1)

## [[ Part 2 ]] ##

def isgear(character):
    return character == '*'

part2 = 0
lines2 = list(lines)

for x in range(len(lines[0])-2):
    for y in range(len(lines)-2):
        if isgear(lines[y][x]):
            indices = get_indices_around_symbol(x,y)
            number_parts = []

            for xx, yy in indices:
                number_parts.append(get_number_at_index(xx,yy,lines2))

            non_null_number_parts = list(filter(lambda x: x>0,number_parts));

            if len(non_null_number_parts) == 2:
                fst = non_null_number_parts[0]
                snd = non_null_number_parts[1]
                part2 += fst * snd

print(part2)
