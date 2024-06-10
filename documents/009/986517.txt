import sys

(a, b, c) = [int(i) for i in sys.stdin.readline().split(' ')]

if a < b < c:
    print("Yes")
else:
    print("No")