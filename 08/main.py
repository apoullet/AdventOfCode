import sys
import math

from itertools import cycle
from functools import partial


with open(sys.argv[1], 'r') as f:
    lines = list(filter(None,map(str.strip, f.readlines())))

instructions = lines[0]
network      = lines[1:]

look_up =  {}
for n in network:
    source, destinations_str = n.split(' = ')
    fst_str, snd_str = destinations_str.split(', ')
    destinations = tuple([fst_str[1:], snd_str[:-1]])
    look_up[source] = destinations

step_count = 0
current_node = 'AAA'

for instruction in cycle(instructions):
    if current_node == 'ZZZ':
        break
    nodes = look_up[current_node]
    new_node = nodes[0] if instruction == 'L' else nodes[1]
    current_node = new_node
    step_count += 1

print(step_count)

def get_loop_length_inner(look_up, instructions, start):
    step_count = 0
    current_node = start
    for instruction in cycle(instructions):
        step_count += 1
        new_node = look_up[current_node][instruction]

        if new_node[-1] == 'Z':
            return step_count
        current_node = new_node

    return 0

step_count = 0
current_nodes = list(filter(lambda k: k[-1] == 'A',look_up.keys()))
instructions_n = list(map(lambda i: 0 if i == 'L' else 1, instructions))

get_loop_length = partial(get_loop_length_inner, look_up, instructions_n)
loop_lengths = map(get_loop_length, current_nodes)

print(math.lcm(*loop_lengths))
