while True:
    s1 = s2 = 0
    n = int(input())
    if n == 0: break
    for i in range(n):
        a, b = map(int, input().strip().split())
        if a > b:
            s1 += a + b
        elif b > a:
            s2 += a + b
        else:
            s1 += a
            s2 += b
    print(s1, s2)