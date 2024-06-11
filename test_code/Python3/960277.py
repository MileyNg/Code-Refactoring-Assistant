import math

while True:
    n = int(input())
    if n == 0: break
    d = list(map(int, input().strip().split()))
    m = sum(d) / n
    print(math.sqrt(sum((x - m)**2 for x in d) / n))