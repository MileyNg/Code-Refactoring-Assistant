import sys

state = True
for s in sys.stdin:
    if state:
        state = not state
        a = list(map(int, s.split()))
    else:
        state = not state
        b = list(map(int, s.split()))
        hit = sum(a[i] == b[i] for i in range(4))
        blow = sum(b[i] in a for i in range(4)) - hit
        print(hit, blow)