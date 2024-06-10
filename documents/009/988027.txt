import sys

while True:
    (x, y) = [int(i) for i in sys.stdin.readline().split(' ')]

    if x == 0 and y == 0:
        break

    if x > y:
        z = x
        x = y
        y = z

    print(x, y)