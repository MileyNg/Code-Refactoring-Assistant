while 1:
	n,k=map(int,raw_input().split())
	if n==0:break
	a=[int(raw_input()) for i in range(n)]
	cur=mx=sum(a[:k])
	for i in range(n-k):
		cur=cur-a[i]+a[i+k]
		mx=max(mx,cur)
	print mx