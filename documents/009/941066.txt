while 1:
	n = input()
	if n == 0: break
	xy = [map(int,raw_input().split()) for i in range(n)]
	S = set(map(tuple,xy))
	ans = 0
	for i in range(n-1):
		x1,y1 = xy[i]
		for j in range(i+1,n):
			x2,y2 = xy[j]
			a = (x2-y2+y1,y2+x2-x1)
			b = (x1-y2+y1,y1+x2-x1)
			if a in S and b in S:
				ans = max(ans,(x1-x2)**2 + (y1-y2)**2)
	print ans