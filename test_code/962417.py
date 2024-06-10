from collections import deque

n, qt = map(int, input().strip().split())
q = deque()
for i in range(n):
    name, time = input().strip().split()
    q.append((name, int(time)))

t = 0
while q:
    name, time = q.popleft()
    if time <= qt:
        t += time
        print(name, t)
    else:
        t += qt
        time -= qt
        q.append((name, time))