def S(i,x,y):
	w = max(x,y)
	return 2*w-A if 2*w >= A else min(S(i+1,x+a[i],y),S(i+1,x,y+a[i]))
while 1:
	n = input()
	if n == 0: break
	a = sorted(map(int,raw_input().split()))[::-1]
	A = sum(a)
	print S(1,a[0],0)