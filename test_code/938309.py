def S(i,x,y):
	if 2*x >= A: return 2*x-A
	if 2*y >= A: return 2*y-A
	return min(S(i+1,x+a[i],y),S(i+1,x,y+a[i]))
while 1:
	n = input()
	if n == 0: break
	a = sorted(map(int,raw_input().split()))[::-1]
	A = sum(a)
	print S(1,a[0],0)