for i in range(int(raw_input())):
	inp = raw_input()
	train = inp[0]
	for i in range(3,len(inp),3):
		if inp[i] not in train:
			if inp[i-1] == ">": train += inp[i]
			else: train = inp[i]+train
	print train