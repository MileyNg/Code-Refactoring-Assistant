import sys

a = [int(i) for i in sys.stdin.readline().split(' ')]

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t

print(' '.join([str(i) for i in a]))