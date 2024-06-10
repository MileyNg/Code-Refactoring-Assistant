a = range(int(raw_input()) + 1)
for i in range(int(raw_input())):
    p, q = map(int, raw_input().split(','))
    a[p], a[q] = a[q], a[p]
for p in a[1:]:
    print p