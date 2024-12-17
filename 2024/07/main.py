import sys


with open(sys.argv[1], 'r') as p_input:
    lines = list(map(str.strip, p_input.readlines()))

def calibration_possible(value, numbers):
    def inner(value, numbers, acc):
        if len(numbers) == 0:
            return value == acc

        return inner(value, numbers[1:], acc + numbers[0]) or inner(value, numbers[1:], acc * numbers[0]) or inner(value, numbers[1:], acc * 10 ** len(str(numbers[0])) + numbers[0])
    return inner(value, numbers[1:], numbers[0]) or inner(value, numbers[1:], numbers[0]) or inner(value, numbers[1:], numbers[0])

total = 0
for line in lines:
    [value, numbers] = line.split(': ')
    value, numbers   = int(value), list(map(int,numbers.split(' ')))
    if calibration_possible(value, numbers):
        total += value

print(total)