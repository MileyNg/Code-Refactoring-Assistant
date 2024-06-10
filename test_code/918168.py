while 2>1:
	try:
		a,b,c,d,e,f = map(float, raw_input().split(" "))
		x=(c*e-b*f)/(e*a-b*d)
		y=(c*d-a*f)/(b*d-e*a)
		print "%.3f %.3f" % (x+0,y+0)
		
	except EOFError:
		break
	except ValueError:
		break