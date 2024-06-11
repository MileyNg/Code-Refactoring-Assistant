while(True):
    x, y = map(int, input().strip().split())
    if x == y == 0: break
    print(min(x, y), max(x, y))