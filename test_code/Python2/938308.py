def S(i,x,y):
	d=2*max(x,y)-sum(a)
	return d if d>=0 else min(S(i+1,x+a[i],y),S(i+1,x,y+a[i]))
while 1:
	if input()==0:break
	a=sorted(map(int,raw_input().split()))[::-1]
	print S(1,a[0],0)