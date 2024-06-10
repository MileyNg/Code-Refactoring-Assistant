cards = {}
n = int(raw_input())
for i in xrange(n):
    cards[raw_input()] = True
for j in 'SHCD':
    for n in xrange(1,14):
        card = j + ' ' + str(n)
        if card not in cards:
            print card