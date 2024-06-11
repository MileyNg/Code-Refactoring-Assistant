while True:
    try:
        line = input()
    except EOFError:
        break

    a = list(map(int, line))
    while len(a) > 1:
        a = [(a[i] + a[i + 1]) % 10 for i in range(len(a) - 1)]
    print(a[0])