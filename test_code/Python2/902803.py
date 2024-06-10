from collections import Counter

c = Counter()
strings = raw_input().lower().split()
for s in strings:
    c[s] += 1
print sorted(c.items(), key=lambda a: a[1], reverse=True)[0][0],
print sorted(c, key=lambda a: len(a), reverse=True)[0]