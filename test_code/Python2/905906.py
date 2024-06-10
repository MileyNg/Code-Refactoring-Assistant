try:
    while True:
        sm = a = float(raw_input())
        for i in range(9):
            if i % 2 == 0:
                a *= 2
            else:
                a /= 3
            sm += a
        print sm
except EOFError:
    pass