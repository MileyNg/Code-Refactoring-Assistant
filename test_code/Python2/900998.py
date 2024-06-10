rank = ["AAA","AA","A","B","C","D","E"]
ref1 = [35.5,37.5,40.0,43.0,50.0,55.0,70.0]
ref2 = [71.0,77.0,83.0,89.0,105.0,116.0,148.0]
while True:
	try:
		time = map(float, raw_input().split())
		for i in range(7):
			if time[0]<ref1[i] and time[1]<ref2[i]:
				print rank[i]
				break
		else:
			print "NA"
	except:
		break