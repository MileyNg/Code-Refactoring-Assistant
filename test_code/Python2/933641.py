def a(v1,v2):
	if v1[0] != v2[0]:
		return (v2[1]-v1[1])/(v2[0]-v1[0])
	else:
		return (v2[1]-v1[1])*(10**10)
		
def convex(v,n):
	k = 0
	d = []
	u = []
	for i in range(n):
		d.append(i)
		u.append(i)
		while len(d) > 2:
			if a(v[d[-3]],v[d[-2]]) < a(v[d[-2]],v[d[-1]]):
				del d[-2]
			else:
				break
		while len(u) > 2:
			if a(v[u[-3]],v[u[-2]]) > a(v[u[-2]],v[u[-1]]):
				del u[-2]
			else:
				break
	return n - len(set(d+u))
	
while 1:
	n = input()
	if n == 0: break
	v = [map(float,raw_input().split(",")) for i in range(n)]
	v = sorted(sorted(v, key = lambda x:x[1]))
	print convex(v,n)