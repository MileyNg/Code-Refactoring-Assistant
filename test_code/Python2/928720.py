u = [raw_input() for i in range(input())]
t = [raw_input() for i in range(input())]
isopen = -1
for id in t:
	if id in u:
		print "Opened by %s"%(id) if isopen < 0 else "Closed by %s"%(id)
		isopen *= -1
	else:
		print "Unknown",id