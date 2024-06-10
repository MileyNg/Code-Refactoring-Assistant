inf = 1e9
n,m = map(int,raw_input().split())
edge = [map(int,raw_input().split()) for i in range(m)]
d = [inf]*n
d[0] = 0
while 1:
	update = 0
	for i in range(m):
		a,b,c = edge[i]
		if d[a] != inf and d[b] > d[a] - c:
			d[b] = d[a] - c
			update = 1
	if update == 0: break
print abs(d[n-1])