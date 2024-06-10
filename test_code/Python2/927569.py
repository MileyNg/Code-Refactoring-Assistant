def dt(t,t1,t2):
	dt = 60*(10*(int(t2[0]) - int(t1[0])) + (int(t2[1]) - int(t1[1]))) + 10*(int(t2[3]) - int(t1[3])) + (int(t2[4]) - int(t1[4]))
	return dt if dt >= t else False
	
n,t = map(int,raw_input().split())
datas = [raw_input().split() for i in range(n)]
ans = []
for i in range(1,n):
	a = dt(t,datas[i-1][2],datas[i][0])
	if a:
		ans.append([datas[i][1], a])
print len(ans)
for i in range(len(ans)):
	print " ".join(map(str,ans[i]))