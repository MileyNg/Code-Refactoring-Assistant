while 1:
	try:
		N,M = map(int,raw_input().split())
		dp = [[0]*(M+1) for i in range(3)]
		bidols = [[raw_input()]+map(int,raw_input().split()) for i in range(N)]
		for bidol in bidols:
			C = bidol[1]
			if C > M:
				continue
			for i in range(3):
				dp[i][C] = max(dp[i][C],bidol[i+2])
				for j in range(M-C+1):
					if dp[i][j]:
						dp[i][j+C] = max(dp[i][j+C],dp[i][j]+bidol[i+2])
		print max(max(dp[0]),max(dp[1]),max(dp[2]))
	except:
		break