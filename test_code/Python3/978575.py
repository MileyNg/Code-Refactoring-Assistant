while True:
    try:
        s = input()
    except EOFError:
        break

    a, b, n = map(int, s.split())
    a %= b
    x = 0
    for i in range(n):
        a *= 10
        if a >= b:
            q, a = divmod(a, b)
            x += q
    print(x)