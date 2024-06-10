for r in range(input()):
	snake=raw_input()
	m=(len(snake)-4)/2
	if m>0 and snake == ">'" + "="*m + "#" + "="*m + "~":
		print "A"
	elif m>0 and snake == ">^" + "Q="*m + "~~":
		print "B"
	else:
		print "NA"