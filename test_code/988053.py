import sys

(a, b, c) = [int(i) for i in sys.stdin.readline().split(' ')]

divisorCount = 0
for d in range(a, b+1):
    if c % d == 0:
        divisorCount += 1

print(divisorCount)