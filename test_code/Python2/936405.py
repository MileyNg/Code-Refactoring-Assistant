global B
def check(B,x,y,c):
	if 0 < x < w+2 and 0 < y < h+2 and B[y][x] == c:
		B[y][x] = -1
		check(B,x-1,y,c);check(B,x,y-1,c);check(B,x+1,y,c);check(B,x,y+1,c)

while 1:
	w,h = map(int,raw_input().split())
	if w == 0: break
	B = [[0]*(w+2) for i in range(h+2)]
	xs,ys = map(int,raw_input().split())
	xg,yg = map(int,raw_input().split())
	for i in range(input()):
		c,d,x,y = map(int,raw_input().split())
		if d == 0:
			B[y][x:x+4] = [c]*4
			B[y+1][x:x+4] = [c]*4
		else:
			for j in range(4):
				B[y+j][x:x+2] = [c]*2
	if B[ys][xs] != B[yg][xg]:
		print "NG"
	else:
		check(B,xs,ys,B[ys][xs])
		print "OK" if B[yg][xg] == -1 else "NG"