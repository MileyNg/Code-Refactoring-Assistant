import sys

def plot(x, y):
    global ban
    if 0 <= x < 10 and 0 <= y < 10: ban[y][x] += 1

def drop(x, y, s):
    for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        plot(x + dx, y + dy)
    if s == 1: return
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        plot(x + dx, y + dy)
    if s == 2: return
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        plot(x + dx, y + dy)

ban = [[0 for x in range(10)] for y in range(10)]
for line in sys.stdin:
    x, y, size = map(int, line.split(','))
    drop(x, y, size)

print(sum(ban[y][x] == 0 for y in range(10) for x in range(10)))
print(max(ban[y][x] for y in range(10) for x in range(10)))