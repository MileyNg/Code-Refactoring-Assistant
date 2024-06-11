v = int(input())
h = int(input())

l = [i for i in range(1, v + 1)]
for i in range(h):
    n, m = input().split(',')
    n = int(n) - 1
    m = int(m) - 1
    l[n], l[m] = l[m], l[n]

for i in l:
    print(i)