while 1:
	n = input()
	if n == 0: break
	datas = [map(int,raw_input().split()) for i in range(n)]
	maxw = 0
	for d1 in datas:
		w = sum([d2[0] for d2 in datas if d2[1]<=d1[1]<d2[2]])
		maxw = max(w,maxw)
	print "OK" if maxw <= 150 else "NG"