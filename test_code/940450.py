dx = [2,2,2,1,0,-1,-2,-2,-2,-1,0,1]
dy = [-1,0,1,2,2,2,1,0,-1,-2,-2,-2]
def solve(x,y,XY):
	xy = XY[:]
	if len(xy) == 0: return "OK"
	sx,sy = xy.pop(0),xy.pop(0)
	for i in range(12):
		try:
			if doa(x+dx[i],y+dy[i],sx,sy): 
				r = solve(x+dx[i],y+dy[i],xy)
				if r: return r
		except:
			pass

def doa(x,y,sx,sy):
	return True if abs(x-sx) < 2 and abs(y-sy) < 2 else False

while 1:
	x,y = map(int,raw_input().split())
	if x == y == 0: break
	n = input()
	xy = map(int,raw_input().split())
	ans = solve(x,y,xy)
	print ans if ans else "NA"