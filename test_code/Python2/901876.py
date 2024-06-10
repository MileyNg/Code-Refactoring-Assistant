while 1:
	b,r,g,c,s,t=map(int,raw_input().split())
	if t==0:break
	print 100+95*b+63*r+7*g+2*c-3*(t-s)