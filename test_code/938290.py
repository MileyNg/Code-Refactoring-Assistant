while 1:
	try:
		N,M = map(int,raw_input().split())
		dp = [[0]*(M+1) for i in range(3)]
		for _ in range(N):
			name = raw_input()
			C,V,D,L = map(int,raw_input().split())
			VDL = [V,D,L]
			for i in range(3):
				try: dp[i][C] = max(dp[i][C],VDL[i])
				except: break
				for j in range(M):
					if dp[i][j]:
						try: dp[i][j+C] = max(dp[i][j+C],dp[i][j]+VDL[i])
						except: break
		print max(max(dp[0]),max(dp[1]),max(dp[2]))
	except:
		break