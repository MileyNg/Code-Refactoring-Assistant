n,m=map(int,raw_input().split())
v=[0]*n
a=[int(raw_input()) for i in [1]*n]
b=[int(raw_input()) for i in [1]*m]
for c in b:
	for i in range(n):
		if a[i]<=c:
			v[i]+=1
			break
print v.index(max(v))+1