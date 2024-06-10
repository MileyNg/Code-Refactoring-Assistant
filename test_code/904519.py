try:
    while True:
        d = int(raw_input())
        sm = 0
        for i in range(d, 600, d):
            sm += (i ** 2) * d
        print sm
except:
    pass