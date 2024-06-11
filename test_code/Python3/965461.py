from itertools import combinations

while True:
    n, s = map(int, input().split())
    if n == s == 0: break

    print(sum(1 for x in combinations(range(10), n) if sum(x) == s))