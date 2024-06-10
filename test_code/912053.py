while 1:
	n,m=map(int,raw_input().split())
	if n==0:break
	h={i:0 for i in range(m)}
	for i in range(n):
		a=map(int,raw_input().split())
		for j in range(m):
			h[j]+=a[j]
	ans=[k[0]+1 for k in sorted(h.items(),key=lambda x:x[1],reverse=True)]
	print " ".join(map(str,ans))