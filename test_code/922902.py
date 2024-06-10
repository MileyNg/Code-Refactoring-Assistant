while 1:
	W,Q = map(int,raw_input().split())
	if W == 0: break
	cat = [map(str,raw_input().split()) for i in range(Q)]
	wall = [-1]*W
	for i in range(Q):
		if cat[i][0] == "s":
			id,w = int(cat[i][1]),int(cat[i][2])
			for j in range(W-w+1):
				if wall[j:j+w] == [-1]*w:
					wall[j:j+w] = [id]*w
					print j
					break
			else:
				print "impossible"
		else:
			flag = 0
			for j in range(W):
				if wall[j] == int(cat[i][1]):
					wall[j] = -1
					flag = 1
				elif flag == 1:
					break
	print "END"