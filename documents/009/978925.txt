while True:
    try:
        s = input()
    except EOFError:
        break

    r = ''
    n = 1
    for c in s:
        if n < 0:
            n = int(c)
        elif c == '@':
            n = -1
        else:
            r += c * n
            n = 1
    print(r)