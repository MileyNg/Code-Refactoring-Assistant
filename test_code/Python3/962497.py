n = int(input())
a = list(map(int, input().strip().split()))
q = int(input())
M = list(map(int, input().strip().split()))

d = []
for x in range(1 << n):
    b = '{:0{}b}'.format(x, n)
    d.append(sum(a[i] for i in range(n) if b[i] == '1'))

for m in M:
    print('yes' if m in d else 'no')