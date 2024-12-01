import sys


lines = list(map(str.strip,open(sys.argv[1]).readlines()))

calories = []
current = answer = 0
for line in lines:
    if line == '':
        calories.append(current)
        answer = max(current, answer)
        current = 0
    else:
        current += int(line)

print(answer)
print(sum(sorted(calories, reverse=True)[:3]))
