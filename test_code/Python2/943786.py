while 1:
	n,p = map(int,raw_input().split())
	if n == 0: break
	have = [0]*n
	stone = p
	i = count = 0
	while 1:
		count += 1
		if stone > 0:
			have[i] += 1
			stone -= 1
		else:
			stone += have[i]
			have[i] = 0
		if have[i] == p:
			break
		i = (i+1)%n
	print i