while 1:
	n,a,b = map(int,raw_input().split())
	if n == 0: break
	dp = [0]*(n+max(a,b)+1)
	dp[a] = dp[b] = 1
	for i in range(n+1):
		if dp[i]:
			dp[i+a] = dp[i+b] = 1
	print n - sum(dp[:n+1])