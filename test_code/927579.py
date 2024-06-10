def dt(t,t1,t2):
	dt = [int(t2[i]) - int(t1[i]) for i in [0,1,3,4]]
	dt = 60*(10*dt[0] + dt[1]) + 10*dt[2] + dt[3]
	return dt if dt >= t else False
	
n,t = map(int,raw_input().split())
s = [raw_input().split() for i in range(n)]
ans = []
for i in range(1,n):
	a = dt(t,s[i-1][2],s[i][0])
	if a:
		ans.append([s[i][1], a])
print len(ans)
for i in range(len(ans)):
	print " ".join(map(str,ans[i]))