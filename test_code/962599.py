n = int(input())
a = []
for i in range(n):
    s, x = input().strip().split()
    a.append((s, int(x)))
for s in 'SHCD':
    for i in range(1, 14):
        if (s, i) not in a:
            print(s, i)