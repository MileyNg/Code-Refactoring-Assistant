from math import * 
R=6378.1
while 1:
	a,b,c,d=map(float,raw_input().split())
	if (a,b,c,d)==(-1,-1,-1,-1):break
	rd=pi/180
	a,b,c,d=a*rd,b*rd,c*rd,d*rd
	cosin=cos(a)*cos(c)*cos(b-d)+sin(a)*sin(c)
	print int(round(R*acos(cosin)))