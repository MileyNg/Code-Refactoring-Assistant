rank = ["AAA","AA","A","B","C","D","E"]
ref0 = [35.5,37.5,40.0,43.0,50.0,55.0,70.0]
ref1 = [71.0,77.0,83.0,89.0,105.0,116.0,148.0]
while True:
	try:
		t = map(float, raw_input().split())
		for i in range(7):
			if t[0]<ref0[i] and t[1]<ref1[i]:
				print rank[i]
				break
		else:
			print "NA"
	except:
		break