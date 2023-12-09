import sys


with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))
    
sequences = [[int(n) for n in line.split(' ')] for line in lines]

def find_next_value(sequence):
    sub_sequences = [list(sequence)]

    while sum(sub_sequences[-1]) != 0:
        last_sequence = sub_sequences[-1]
        new_sequence = list(map(lambda p: p[1]-p[0], zip(last_sequence[:-1], last_sequence[1:])))
        sub_sequences.append(new_sequence)

    for i, _ in enumerate(sub_sequences[:-1][::-1]):
        previous = sub_sequences[-2-i+1][-1]
        sub_sequences[-2-i].append(sub_sequences[-2-i][-1] + previous)
    
    return sub_sequences[0][-1]

print(sum(map(find_next_value, sequences)))

def find_previous_value(sequence):
    sub_sequences = [list(sequence)]

    while sum(sub_sequences[-1]) != 0:
        last_sequence = sub_sequences[-1]
        new_sequence = list(map(lambda p: p[1]-p[0], zip(last_sequence[:-1], last_sequence[1:])))
        sub_sequences.append(new_sequence)

    for i, _ in enumerate(sub_sequences[:-1][::-1]):
        previous = sub_sequences[-2-i+1][0]
        sub_sequences[-2-i].insert(0, sub_sequences[-2-i][0] - previous)
    
    return sub_sequences[0][0]

print(sum(map(find_previous_value, sequences)))
