try:
    while True:
        a = map(int, raw_input())
        for i in range(9, 0, -1):
            for j in range(i):
                a[j] = (a[j] + a[j + 1]) % 10
        print a[0]
except EOFError:
    pass