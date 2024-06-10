from collections import Counter
c = Counter()
while 1:
    try:
        c[input()] += 1
    except:
        break
L = sorted(c.items(), key=lambda a:(-a[1], a[0]))
mx = L[0][1]
for x in L:
    if x[1] == mx:
        print x[0]
    else:
        break