while 1:
	n = input()
	if n == 0: break
	taro = sorted([input() for i in range(n)])
	hana = [i for i in range(1,2*n+1) if i not in taro]
	field = 0
	while hana:
		for i in range(len(taro)):
			if taro[i] > field:
				field = taro.pop(i)
				break
		else:
			field = 0
		if len(taro) == 0: break
		for i in range(len(hana)):
			if hana[i] > field:
				field = hana.pop(i)
				break
		else:
			field = 0
	print len(hana)
	print len(taro)