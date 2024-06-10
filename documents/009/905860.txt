try:
    a, b = [], []
    while True:
        p, q = map(int, raw_input().split(','))
        a.append(p * q)
        b.append(q)
except EOFError:
    pass
print sum(a)
print int(round(float(sum(b)) / len(b)))