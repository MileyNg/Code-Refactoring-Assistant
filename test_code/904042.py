while True:
	n, x = map(int, raw_input().split())
	if n + x == 0: break
	ans = 0
	for i in range(1,n-1):
		for j in range(i+1, n):
			for h in range(j+1, n+1):
				if i + j + h == x: ans += 1
	print ans