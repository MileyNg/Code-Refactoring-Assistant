while 1:
	n,a,b = map(int,raw_input().split())
	if n == 0: break
	dp = [0]*(n+1)
	if a < n+1: dp[a] = 1
	if b < n+1: dp[b] = 1
	for i in range(n+1):
		if dp[i]:
			if i+a < n+1: dp[i+a] = 1
			if i+b < n+1: dp[i+b] = 1
	print n - sum(dp)