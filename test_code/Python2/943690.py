W,H = 12,12
dxy = [[1,0],[0,1],[-1,0],[0,-1]]
def solve(field,w,h):
	if 0 <= w < W and 0 <= h < H and field[h][w] == "1":
		field[h][w] = "0"
		for dx,dy in dxy:
			solve(field,w+dx,h+dy)

while 1:
	try:
		field = [list(raw_input()) for i in range(H)]
		ans = 0
		for h in range(H):
			for w in range(W):
				if field[h][w] == "1":
					solve(field,w,h)
					ans += 1
		print ans
		raw_input()
	except:
		break