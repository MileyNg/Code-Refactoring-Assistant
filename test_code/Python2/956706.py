from collections import Counter

trade1 = Counter()
trade2 = Counter()
while 1:
    line = raw_input()
    if not line:
        break
    a, b = map(int, line.split(','))
    trade1[a] += 1

while 1:
    try:
        a, b = map(int, raw_input().split(','))
    except EOFError:
        break
    trade2[a] += 1

trade = trade1 + trade2
for k in sorted(trade1 & trade2):
    print k, trade[k]