Ball = {'A': 1, 'B': 0, 'C': 0}
while 1:
    try:
        a, b = raw_input().split(',')
    except EOFError:
        break
    Ball[a], Ball[b] = Ball[b], Ball[a]
for b in Ball:
    if Ball[b] == 1:
        print b