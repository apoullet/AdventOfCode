import sys

from functools import cmp_to_key, partial, reduce


with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip,f.readlines()))

hands_to_bids = { hand: int(bid) for hand, bid in map(lambda l: l.split(' '), lines) }

def get_bid(hand_with_rank):
    hand = hand_with_rank[0]
    return hands_to_bids[hand]

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

card_ranks_j = { **card_ranks, 'J': 13 }

hand_ranks = {
    5: 0,
    41: 1,
    32: 2,
    311: 3,
    221: 4,
    2111: 5,
    11111: 6
}

def get_hand_with_type(hand):
    index = {}
    for card in hand:
        if card in index:
            index[card] += 1
        else:
            index[card] = 1

    key = reduce(lambda a, c: a * 10 + c, sorted(index.values(), reverse=True))
    return (hand, hand_ranks[key])

def compare_hands_inner(card_ranks, fst, snd):
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

compare_hands = partial(compare_hands_inner, card_ranks)

sorted_bids = map(get_bid, sorted(map(get_hand_with_type, hands_to_bids.keys()), key=cmp_to_key(compare_hands)))

part_1 = reduce(lambda a, c: a + c[0] * c[1], enumerate(sorted_bids, 1), 0)

print(part_1)

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

    key = reduce(lambda a, c: a * 10 + c, sorted_hand)
    return (hand, hand_ranks[key])

compare_hands_j = partial(compare_hands_inner, card_ranks_j)

sorted_bids_j = map(get_bid, sorted(map(get_hand_with_type_j, hands_to_bids.keys()), key=cmp_to_key(compare_hands_j)))

part_2 = reduce(lambda a, c: a + c[0] * c[1], enumerate(sorted_bids_j, 1), 0)

print(part_2)
