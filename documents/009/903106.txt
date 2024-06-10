for i in [1]*input():
	c,a,n=map(int,raw_input().split())
	s=0
	while c>0 and a>0 and n>0:
		s,c,a,n=s+1,c-1,a-1,n-1
	while c>0 and a>0:
		s,c,a=s+1,c-2,a-1
	print s+c/3