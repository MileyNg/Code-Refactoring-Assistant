a,b=3600,60
for i in [1]*3:
	h,m,s,x,y,z=map(int,raw_input().split())
	s=(x-h)*a+(y-m)*b+(z-s)
	print s//a,s%a//b,s%b