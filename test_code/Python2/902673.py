n=range(input())
a=[map(int,raw_input().split()) for i in n]
s=[0]*len(n)
for i in [0,1,2]:
	for j in n:
		for k in n:
			if j!=k and a[j][i]==a[k][i]:break
		else:s[j]+=a[j][i]
for i in s:print i