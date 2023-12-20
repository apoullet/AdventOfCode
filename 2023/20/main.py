import sys
import math

from collections import deque


def read_lines(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip().split('\n')

def check(actual, expected):
    if actual != expected:
        print(f"Wrong answer! Expected {'{:,}'.format(expected)} but got {'{:,}'.format(actual)} instead.")
    else:
        print(f"Got {'{:,}'.format(expected)} which is the correct answer :)")

def solve(lines, part2 = False):
    lp_count = hp_count = 0

    table = {}
    for line in lines:
        input, outputs = line.split(' -> ')
        outputs        = outputs.split(', ')

        match input[0], input[1:]:
            case ('%', ff):
                table[ff] = ('%', 'off', outputs)
            case ('&', con):
                table[con] = ('&', {}, outputs)
            case _:
                table[input] = ('b', None, outputs)

    cons = set()
    for in_, out_ in table.items():
        kind, _, _ = out_

        if kind == '&':
            cons.add(in_)

    for in_, out_ in table.items():
        kind, _, outputs = out_

        if kind != '&':
            for output in outputs:
                if output in cons:
                    table[output][1][in_] = 'off'

    q = deque()

    tr = {}

    for i in range(1000 if part2 is False else sys.maxsize):
        q.append(['button', 'lo', 'broadcaster'])

        while len(q) > 0:
            in_, pulse, cur_ = q.popleft()

            if cur_ == 'rx':
                _, state, _ = table[in_]

                for in_2, value in state.items():
                    if value == 'hi':
                        if in_2 not in tr:
                            tr[in_2] = i+1

                        if all(map(lambda o: o in tr, state.keys())):
                            return math.lcm(*tr.values())

            if pulse == 'lo':
                lp_count += 1
            else:
                hp_count += 1

            if cur_ not in table:
                if cur_ == 'rx' and pulse == 'lo':
                    return i+1
                continue

            kind, state, outputs = table[cur_]

            match kind:
                case '%':
                    if pulse == 'hi':
                        continue
                    if state == 'off':
                        for output in outputs:
                            q.append([cur_, 'hi', output])
                        table[cur_] = (kind, 'on', outputs)
                    else:
                        for output in outputs:
                            q.append([cur_, 'lo', output])
                        table[cur_] = (kind, 'off', outputs)
                case '&':
                    state[in_] = pulse
                    if all(map(lambda p: p == 'hi', state.values())):
                        for output in outputs:
                            q.append([cur_, 'lo', output])
                    else:
                        for output in outputs:
                            q.append([cur_, 'hi', output])
                case 'b':
                    for output in outputs:
                        q.append([cur_, 'lo', output])
    return lp_count * hp_count

check(solve(read_lines('example1.txt')), 32_000_000)
check(solve(read_lines('example2.txt')), 11_687_500)

print(solve(read_lines('input.txt')))
print(solve(read_lines('input.txt'), True))
