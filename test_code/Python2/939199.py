def getxy(P,x,y,ans):
	for dy in range(m):
		for dx in range(m):
			if P[dy][dx] > -1:
				xy = [x+dx+1,y+dy+1]
				if ans == "NA" or xy[1] < ans[1] or (xy[1] == ans[1] and xy[0] < ans[0]):
					return xy
				else:
					return ans

# try-except is necessary
while 1:
	try:
		n,m = map(int,raw_input().split())
		if n == 0: break
		S = [map(int,raw_input().split()) for i in range(n)]
		P = [map(int,raw_input().split()) for i in range(m)]

		ans = "NA"
		for rot in range(4):
			if S == P:
				ans = getxy(P,0,0,ans)
			for y in range(n-m+1):
				for x in range(n-m+1):
					flag = 0
					for dy in range(m):
						for dx in range(m):
							if P[dy][dx] > -1 and S[y+dy][x+dx] - P[dy][dx] != 0:
								flag = 1
								break
						if flag == 1: break
					if flag == 0:
						ans = getxy(P,x,y,ans)
						break
				if flag == 0: break
			P = [[P[j][i] for j in range(m-1,-1,-1)] for i in range(m)]
		print ans if ans == "NA" else " ".join(map(str,ans))
	except:
		pass