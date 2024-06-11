import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
for i in range(n):
    cmd = sys.stdin.readline()[:-1]
    if cmd[0] == 'i':
        q.appendleft(cmd[7:])
    elif cmd[6] == ' ':
        try:
            q.remove(cmd[7:])
        except:
            pass
    elif cmd[6] == 'F':
        q.popleft()
    else:
        q.pop()

print(' '.join(q))