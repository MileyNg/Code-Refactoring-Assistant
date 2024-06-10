raws, columns = map(int, input().strip().split())
a = []
for i in range(raws):
    a.append(list(map(int, input().strip().split())))
for i in range(raws):
    a[i].append(sum(a[i]))
a.append([sum(i) for i in zip(*a)])
for r in a:
    print(' '.join(str(x) for x in r))