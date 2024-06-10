def f(b):
    a = [0, 0]
    for p in b:
        if p > a[1]:
            a[1] = p
        elif p > a[0]:
            a[0] = p
        else:
            return False
        a.sort()
    return True

for i in range(int(raw_input())):
    print 'YES' if f(map(int, raw_input().split())) else 'NO'