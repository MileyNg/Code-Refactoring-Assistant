while 1:
	n,m=map(int,raw_input().split())
	if n==0:break
	field=[int(raw_input()) for i in range(n)]
	dice=[int(raw_input()) for i in range(m)]
	now=0
	for i in range(m):
		now+=dice[i]
		try:now+=field[now]
		except:pass
		if now>=n-1:
			print i+1
			break