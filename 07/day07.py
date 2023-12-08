from collections import Counter

hands = []
bids = []

with open('./input_all.txt') as f:
    for line in f:
        hand, bid = line.strip().split(' ')
        bid = int(bid)
        hands.append(hand)
        bids.append(bid)

hand_types = []
for i in range(len(hands)):
    hand = hands[i]
    bid = bids[i]
    
    counts = Counter(hand)
    max_count = max(counts.values())
    unique_count = set(counts.values())
    count_of_counts = Counter(counts.values())
    if max_count ==5:
        hand_types.append('five_of_a_kind')
    elif max_count == 4:
        hand_types.append('four_of_a_kind')
    elif max_count == 3:
        # check if it is full house
        if 2 in unique_count:
            hand_types.append('full_house')
        else:
            hand_types.append('three_of_a_kind')
    elif max_count == 2:
        # check if it is two pair
        if count_of_counts[2] == 2:
            hand_types.append('two_pair')
        else:
            hand_types.append('one_pair')
    else:
        hand_types.append('high_card')

# now rank the hands
hand_ranks = {
    'five_of_a_kind': [],
    'four_of_a_kind': [],
    'full_house': [],
    'three_of_a_kind': [],
    'two_pair': [],
    'one_pair': [],
    'high_card': []
}

for i in range(len(hands)):
    hand = hands[i]
    hand_type = hand_types[i]
    bid = bids[i]
    hand_ranks[hand_type].append((hand, bid))


card_order = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}
def has_higher_hands(l1, l2):
    print('comparing', l1, l2)
    h1 = l1[0]
    h2 = l2[0]
    for c1, c2 in zip(h1, h2):
        if c1 == c2:
            continue
        else:
            return card_order[c1] > card_order[c2]
        
def custom_buble_sort_desc(l, compare_func):
    n = len(l)
    for i in range(n):
        for j in range(n-i-1):
            if not compare_func(l[j], l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
    return l

winnings = 0
curr_rank = len(hands) # assign from higest rank first
for hand_type, l in hand_ranks.items():
    if len(l) == 0:
        continue
    elif len(l) == 1:
        print(l[0], curr_rank)
        winnings += l[0][1]*curr_rank
        curr_rank -= 1
    else:
        # ties, first sort l using bubble sort, sort in descending order
        print('ties', l)
        l = custom_buble_sort_desc(l, has_higher_hands)

        for hand, bid in l:
            print(hand, bid, curr_rank)
            winnings += bid*curr_rank
            curr_rank -= 1

print(winnings)

