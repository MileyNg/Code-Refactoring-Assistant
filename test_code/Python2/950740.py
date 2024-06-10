n = input()
ax = ay = x = y = mx = 0
while n > 0:
	dx,dy = map(int,raw_input().split())
	if dx == dy == 0:
		print ax,ay
		n -= 1
		ax = ay = x = y = mx = 0
		continue
	x += dx; y += dy
	if x*x + y*y > mx:
		mx = x**2 + y**2
		ax,ay = x,y
	elif x*x + y*y == mx:
		if x > ax:
			ax,ay = x,y