t = input()
q = [0]*(t + 1)
for i in range(t + 1):
	n,m = map(int,raw_input().split())
	vr = [map(float,raw_input().split()) for x in range(m)]
	q[i] = sum([v*r for v,r in vr])/sum([r for v,r in vr]) 
q = [q[i] - q[-1] for i in range(t + 1)]
print "YES" if max(q) > 0.0000001 else "NO"