cards = {'S': set(range(1, 14)),
         'H': set(range(1, 14)),
         'C': set(range(1, 14)),
         'D': set(range(1, 14)), }
for i in range(input()):
    suit, num = raw_input().split()
    cards[suit].discard(int(num))
for suit in "SHCD":
    for c in cards[suit]:
        print suit, c