with open('input.txt', 'r') as f:
    lines = list(map(str.strip,f.readlines()))

total = 0
for line in lines:
    game = line.split(": ")[1]
    winning, mine = game.split(" | ")

    winning_set = set(map(int,filter(None,winning.split(' '))))
    mine_set    = set(map(int,filter(None,mine.split(' '))))

    intersection = winning_set.intersection(mine_set)

    if len(intersection) > 0:
        total += 2 ** (len(intersection)-1)

print("Part 1:",total)

memo = {}

def count_scratchcards(lines, index):
    if index > len(lines):
        return 0

    if index in memo:
        winning_numbers_count = memo[index]
    else:
        line = lines[index]
        game = line.split(": ")[1]
        winning, mine = game.split(" | ")

        winning_set = set(map(int,filter(None,winning.split(' '))))
        mine_set    = set(map(int,filter(None,mine.split(' '))))

        winning_numbers_count = len(winning_set.intersection(mine_set))
        memo[index] = winning_numbers_count

    if winning_numbers_count == 0:
        return 1

    return 1 + sum([count_scratchcards(lines, i) for i in range(index + 1, index + winning_numbers_count + 1)])

print("Part 2:",sum([count_scratchcards(lines, i) for i in range(len(lines))]))
