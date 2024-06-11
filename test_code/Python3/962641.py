while True:
    t = input().strip()
    if t == '-': break
    n = int(input())
    for i in range(n):
        h = int(input())
        t = t[h:] + t[:h]
    print(t)