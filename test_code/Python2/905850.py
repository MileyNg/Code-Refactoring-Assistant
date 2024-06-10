def f(a):
    if a == [0] * 10:
        return True

    for i in range(1, 10):
        if a[i] < 3: continue
        b = list(a)
        b[i] -= 3
        if f(b):
            return True

    for i in range(3, 10):
        if a[i - 2] == 0 or a[i - 1] == 0 or a[i] == 0: continue
        b = list(a)
        for j in range(i - 2, i + 1):
            b[j] -= 1
        if f(b):
            return True
    return False

try:
    while True:
        a = [0] * 10
        for c in raw_input():
            a[int(c)] += 1
        d = []
        for i in range(1, 10):
            if a[i] == 4: continue
            b = list(a)
            b[i] += 1
            for j in range(1, 10):
                if b[j] < 2: continue
                c = list(b)
                c[j] -= 2
                if f(c):
                    d.append(str(i))
                    break
        print ' '.join(d) if d else 0
except EOFError:
    pass