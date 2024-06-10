def delta(t1,t2):
	dt = [int(t2[i]) - int(t1[i]) for i in [0,1,3,4]]
	dt = 60*(10*dt[0] + dt[1]) + 10*dt[2] + dt[3]
	return dt
	
n,t = map(int,raw_input().split())
s = [raw_input().split() for i in range(n)]
a = []
for i in range(1,n):
	dt = delta(s[i-1][2],s[i][0])
	if dt >= t:
		a.append([s[i][1],str(dt)])
print len(a)
for i in a:
	print " ".join(i)