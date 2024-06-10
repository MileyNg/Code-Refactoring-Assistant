b,w = ["b"]*3,["w"]*3
t = range(3)
while 1:
	try:
		bw = [list(raw_input()) for i in t]
		ans = "NA"
		for i in range(3):
			if b == bw[i] or b == [bw[j][i] for j in t]: ans = "b"
			if w == bw[i] or w == [bw[j][i] for j in t]: ans = "w"
		if b == [bw[i][i] for i in t] or b == [bw[i][2-i] for i in t]: ans = "b"
		if w == [bw[i][i] for i in t] or w == [bw[i][2-i] for i in t]: ans = "w"
		print ans
	except:
		break