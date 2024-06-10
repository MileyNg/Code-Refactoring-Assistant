size = [60,80,100,120,140,160]
weight = [2,5,10,15,20,25]
cost = [6,8,10,12,14,16]
while True:
	n = int(raw_input())
	if n == 0: break
	ans = 0
	for i in range(n):
		x,y,h,w = map(int, raw_input().split())
		xyh = x+y+h
		for j in range(6):
			if xyh <= size[j] and w <= weight[j]:
				ans += cost[j]*100
				break
	print ans