from math import sqrt

while True:
    n = int(input())
    if n == 0: break
    a = list(map(int, input().strip().split()))
    print(sqrt(n * sum(x*x for x in a) - sum(a)**2)/n)