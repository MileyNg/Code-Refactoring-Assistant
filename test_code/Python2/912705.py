import math
def S(a,b,c):
	s = (a+b+c)/2
	return math.sqrt(s*(s-a)*(s-b)*(s-c))
	
while True:
	try:
		x1,y1,x2,y2,x3,y3,xp,yp = map(float, raw_input().split())
		a = math.sqrt((x1-x2)**2+(y1-y2)**2)
		b = math.sqrt((x1-x3)**2+(y1-y3)**2)
		c = math.sqrt((x2-x3)**2+(y2-y3)**2)
		xa = math.sqrt((x3-xp)**2+(y3-yp)**2)
		xb = math.sqrt((x2-xp)**2+(y2-yp)**2)
		xc = math.sqrt((x1-xp)**2+(y1-yp)**2)
		if S(a,xb,xc)+S(b,xc,xa)+S(c,xa,xb)-S(a,b,c) > 0.0000001:
			print "NO"
		else:
			print "YES"
	except:
		break