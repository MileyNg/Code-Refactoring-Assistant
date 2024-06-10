import sys

(a, b) = [int(i) for i in sys.stdin.readline().split(' ')]

if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")