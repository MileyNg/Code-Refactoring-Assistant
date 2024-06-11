while True:
    try:
        s = input()
    except EOFError:
        break

    a = float(s)
    x = 0
    for i in range(5):
        x += a
        a *= 2
        x += a
        a /= 3
    print(x)