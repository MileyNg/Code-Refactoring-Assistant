w = int(input())
x = [i for i in range(w + 1)]
n = int(input())
for i in range(n):
    a, b = map(int, input().split(','))
    x[a], x[b] = x[b], x[a]
for i in range(1, w + 1):
    print(x[i])