L = []
for i in range(input()):
    L.append(map(int, raw_input().split()))
print ' '.join(map(str, sorted(L, key=lambda a:(-a[1], a[0]))[0]))