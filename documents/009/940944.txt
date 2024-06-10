dic = {"0":0,"1":1,"2":2}
while 1:
	worm = raw_input()
	if worm == "0": break
	worm = worm.replace("r","0").replace("g","1").replace("b","2")
	n = len(worm)
	ref = ["0"*n,"1"*n,"2"*n]
	done = [1]*(3**n)
	done[int(worm,3)] = 0
	cnt = flag = 0
	nxtque = [worm]
	while 1:
		que = nxtque
		nxtque = []
		for Worm in que:
			if Worm in ref:
				flag = 1
				break
			for i in range(n-1):
				if Worm[i] != Worm[i+1]:
					nextclr = "012"[3-dic[Worm[i]]-dic[Worm[i+1]]]
					worm = Worm[:i] + 2*nextclr + Worm[i+2:]
					num = int(worm,3)
					if done[num]:
						done[num] = 0
						nxtque.append(worm)
		if flag or len(nxtque) == 0: break
		cnt += 1
	print cnt if flag else "NA"