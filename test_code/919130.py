from math import *

def S(p):
	return sum([sin(a*pi/180) for a in p])+sin((360-sum(p))*pi/180)

while 1:
	try:
		p1=[int(raw_input()) for i in range(input()-1)]
		p2=[int(raw_input()) for i in range(input()-1)]
		s1,s2=S(p1),S(p2)
		if    s1-s2>1e-10: print 1
		elif  s2-s1>1e-10: print 2
		else:print 0
	except:break