W,H,N = map(int,raw_input().split())
ans = 0
X,Y = map(int,raw_input().split())
for i in range(N-1):
	X1,Y1 = map(int,raw_input().split())
	dX,dY = X1-X,Y1-Y
	s = 0 if dX*dY > 0 else 1
	ans += max(abs(dY),abs(dX)) + s*min(abs(dY),abs(dX))
	X,Y = X1,Y1
print ans