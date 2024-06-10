while 1:
	N = map(int,raw_input().split())
	if sum(N) == 0: break
	a,b,c = N[0]+N[3],N[1]+N[4],N[2]+N[5]
	m = min(a,b,c)
	ans = 0
	for i in range(max(0,m-2),m+1):
		ans = max(ans,i+(a-i)/3+(b-i)/3+(c-i)/3)
	print ans