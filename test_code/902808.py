from itertools import combinations
while 1:
    n, s = map(int, raw_input().split())
    if n == s == 0:
        break
    print sum(1 for tmp in combinations(range(10), n) if s == sum(tmp))