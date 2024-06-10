while 1:
    n = input()
    if n == 0:
        break
    L = map(float, raw_input().split())
    avg = sum(L) / len(L)
    print (sum((x - avg) ** 2 for x in L) / n) ** 0.5