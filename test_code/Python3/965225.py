while True:
    n = int(input())
    if n == 0: break
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(1, n):
        a[i] = max(a[i - 1] + a[i], a[i])
    print(max(a))