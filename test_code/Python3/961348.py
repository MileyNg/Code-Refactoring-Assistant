maxv = -2*10**9
minv = 2*10**9
n = int(input())
for i in range(n):
    x = int(input())
    maxv = max(x - minv, maxv)
    minv = min(x, minv)
print(maxv)