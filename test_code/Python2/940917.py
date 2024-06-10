dic = {"r":1,"g":2,"b":3}
while 1:
	worm = raw_input()
	if worm == "0": break
	n = len(worm)
	ref = ["r"*n,"g"*n,"b"*n]
	cnt = flag = 0
	queset = set([worm])
	done = set()
	while 1:
		que = list(queset)
		queset = set()
		for Worm in que:
			if Worm in ref:
				flag = 1
				break
			for i in range(n-1):
				if Worm[i] != Worm[i+1]:
					nextclr = "rgb"[5-dic[Worm[i]]-dic[Worm[i+1]]]
					queset.add(Worm[:i] + 2*nextclr + Worm[i+2:])
		if flag or cnt > 14: break
		cnt += 1
		queset -= done
		done |= queset
	print cnt if flag else "NA"