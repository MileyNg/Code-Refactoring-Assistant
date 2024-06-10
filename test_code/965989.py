from itertools import permutations

def g(a):
    if len(a) == 1: yield str(a[0])
    for i in range(1, len(a)):
        for l in g(a[:i]):
            for r in g(a[i:]):
                yield '({}+{})'.format(l, r)
                yield '({}-{})'.format(l, r)
                yield '({}*{})'.format(l, r)

def solve(a):
    for e in permutations(a):
        for s in g(e):
            if eval(s) == 10: return s
    return '0'

while True:
    a = list(map(int, input().split()))
    if a == [0,0,0,0]: break
    print(solve(a))