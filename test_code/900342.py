while True:
	try:
		y, m, d = map(int, raw_input().split())
		date = int("{}{}{}".format('%04d'%y,'%02d'%m,'%02d'%d))
		if date < 18680908:
			print "pre-meiji"
		elif date < 19120730:
			y = y - 1868 + 1
			print "meiji {} {} {}".format(y,m,d)
		elif date < 19261225:
			y = y - 1912 + 1
			print "taisho {} {} {}".format(y,m,d)
		elif date < 19890108:
			y = y - 1926 + 1
			print "showa {} {} {}".format(y,m,d)
		else:
			y = y - 1989 + 1
			print "heisei {} {} {}".format(y,m,d)
	except:
		break