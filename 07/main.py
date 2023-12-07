import sys

from functools import cmp_to_key

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip,f.readlines()))

card_ranks = {
    'A': 0,
    'K': 1,
    'Q': 2,
    'J': 3,
    'T': 4,
    '9': 5,
    '8': 6,
    '7': 7,
    '6': 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12,
}

hand_ranks = {
    '5': 0,
    '41': 1,
    '32': 2,
    '311': 3,
    '221': 4,
    '2111': 5,
    '11111': 6
}

def get_hand_with_type(hand):
    index = {}
    for card in hand:
        if card in index:
            index[card] += 1
        else:
            index[card] = 1

    hand_str = ''.join(sorted(''.join(map(str,index.values())), reverse=True))
    return (hand, hand_ranks[hand_str])

def compare_hands(fst, snd):
    if fst[1] < snd[1]:
        return 1
    elif fst[1] > snd[1]:
        return -1
    else:
        for f, s in zip(fst[0], snd[0]):
            if card_ranks[f] < card_ranks[s]:
                return 1
            elif card_ranks[f] > card_ranks[s]:
                return -1
        return 0

hands_to_bids = { hand: int(bid) for hand, bid in map(lambda l: l.split(' '), lines) }

hands_with_types = list(map(get_hand_with_type, hands_to_bids.keys()))

hands_with_types.sort(key=cmp_to_key(compare_hands))

total = 0
for rank, (hand, _) in enumerate(hands_with_types, 1):
    total += rank * hands_to_bids[hand]

print(total)

card_ranks_j = {
    'A': 0,
    'K': 1,
    'Q': 2,
    'J': 3,
    'T': 4,
    '9': 5,
    '8': 6,
    '7': 7,
    '6': 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12,
    'J': 13,
}

def get_hand_with_type_j(hand):
    index = {}
    for card in hand:
        if card in index:
            index[card] += 1
        else:
            index[card] = 1

    j_value = 0
    if 'J' in index:
        j_value = index['J']
        del index['J']

    if len(index) == 0:
        return (hand, 0)

    sorted_hand = sorted(index.values(), reverse=True)
    sorted_hand[0] += j_value

    hand_str = ''.join(map(str, sorted_hand))
    return (hand, hand_ranks[hand_str])

def compare_hands_j(fst, snd):
    if fst[1] < snd[1]:
        return 1
    elif fst[1] > snd[1]:
        return -1
    else:
        for f, s in zip(fst[0], snd[0]):
            if card_ranks_j[f] < card_ranks_j[s]:
                return 1
            elif card_ranks_j[f] > card_ranks_j[s]:
                return -1
        return 0

hands_with_types_j = list(map(get_hand_with_type_j, hands_to_bids.keys()))
hands_with_types_j.sort(key=cmp_to_key(compare_hands_j))

total_j = 0
for rank, (hand, _) in enumerate(hands_with_types_j, 1):
    total_j += rank * hands_to_bids[hand]

print(total_j)
