from math import *

def S(p):
	return sum([sin(angle*pi/180)/2 for angle in p])

while 1:
	m=input()
	if m==0:break
	p1=[int(raw_input()) for i in range(m-1)]
	p1.append(360-sum(p1))
	n=input()
	p2=[int(raw_input()) for i in range(n-1)]
	p2.append(360-sum(p2))
	s1,s2=S(p1),S(p2)
	if    s1-s2>1e-10: print 1
	elif  s2-s1>1e-10: print 2
	else:print 0