def a(v1,v2):
	if v1[0] != v2[0]:
		return (v2[1]-v1[1])/(v2[0]-v1[0])
	else:
		return (v2[1]-v1[1])*(10**10)
def dlt(p,v,sign):
	while len(p) > 2:
		if sign*(a(v[p[-3]],v[p[-2]]) - a(v[p[-2]],v[p[-1]])) < 0:
			del p[-2]
		else:
			break
	return p
def convex(v,n):
	d,u = [],[]
	for i in range(n):
		d = dlt(d+[i],v,1)
		u = dlt(u+[i],v,-1)
	return n - len(set(d+u))
while 1:
	n = input()
	if n == 0: break
	v = [map(float,raw_input().split(",")) for i in range(n)]
	v = sorted(sorted(v, key = lambda x:x[1]))
	print convex(v,n)