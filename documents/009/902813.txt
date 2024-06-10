r1, r2 = 0, 0
while 1:
    try:
        a, b, c = map(int, raw_input().split(','))
        if a ** 2 + b ** 2 == c ** 2:
            r1 += 1
        elif a == b:
            r2 += 1
    except:
        break
print r1
print r2