try:
    p = q = 0
    while True:
        a, b, c = map(int, raw_input().split(','))
        if a ** 2 + b ** 2 == c ** 2:
            p += 1
        if a == b:
            q += 1
except:
    pass
print p
print q