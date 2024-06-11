dw = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
dm = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

while True:
    m, d = map(int, input().split())
    if m == d == 0: break

    total = sum(dm[i] for i in range(m - 1)) + d - 1
    print(dw[(total + 4) % 7])