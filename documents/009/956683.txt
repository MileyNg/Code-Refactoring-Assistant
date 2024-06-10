while 1:
    try:
        a, b, c = map(float, raw_input().split(','))
    except EOFError:
        break
    if b / c ** 2 >= 25:
        print int(a)