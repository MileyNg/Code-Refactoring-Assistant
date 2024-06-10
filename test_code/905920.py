try:
    a = range(10010)
    a[0] = 1
    for i in range(1, len(a)):
            a[i] += a[i - 1]
    while True:
        print a[int(raw_input())]
except EOFError:
    pass