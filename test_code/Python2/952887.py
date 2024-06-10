W,H,N = map(int,raw_input().split())
ans = 0
x,y = map(int,raw_input().split())
for i in range(N-1):
	X,Y = map(int,raw_input().split())
	dx,dy = X-x,Y-y
	ans += max(abs(dy),abs(dx)) + max(0,min(1,-dx*dy))*min(abs(dy),abs(dx))
	x,y = X,Y
print ans