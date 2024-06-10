while True:
	h, w = map(int, raw_input().split())
	if h + w == 0: break
	b = [list(raw_input()) for i in range(h)]
	x = y = 0
	while True:
		a = b[y][x]
		b[y][x] = 0
		if a == ">": x += 1
		elif a == "<": x -= 1
		elif a == "v": y += 1
		elif a == "^": y -= 1
		elif a == ".": print x,y; break
		else: print "LOOP"; break