import sys

(W, H, x, y, r) = [int(i) for i in sys.stdin.readline().split(' ')]

if x - r >= 0 and x + r <= W and y - r >= 0 and y + r <= H:
    print("Yes")
else:
    print("No")