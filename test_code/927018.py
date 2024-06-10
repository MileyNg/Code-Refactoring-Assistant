r,x = 51,2**31
wc = [[15,2244],[10,1520],[12,1870],[5,850],[3,550],[2,380]]
dp = [x]*r
for w,c in wc:
	dp[w] = c
	for i in range(r - w):
		if dp[i] < x and dp[i + w] > dp[i] + c:
			dp[i + w] = dp[i] + c

while 1:
	n = input()
	if n == 0: break
	print dp[n/100]