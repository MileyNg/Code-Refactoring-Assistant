def f(mn, n, sm):
    if n == 0 and sm == 0:
        return 1
    if mn == 10 or n == 0:
        return 0
    ct = 0
    for i in range(mn, min(10, sm + 1)):
        ct += f(i + 1, n - 1, sm - i)
    return ct

while True:
    n, sm = map(int, raw_input().split())
    if n == 0 and sm == 0:
        break
    print f(0, n, sm)