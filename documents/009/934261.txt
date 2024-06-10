while 1:
	a,type = raw_input().split()
	if type == "X": break
	ans = ""
	if type == "U":
		for word in a.split("_"):
			ans += word[0].upper() + word[1:]
	elif type == "L":
		for word in a.split("_"):
			ans += word[0].upper() + word[1:]
		ans = ans[0].lower() + ans[1:]
	else:
		if "_" not in a:
			words = []
			sp = 0
			for i in range(1,len(a)):
				if a[i].isupper() :
					words.append(a[sp:i].lower())
					sp = i
			words.append(a[sp:].lower())
			ans = "_".join(words)
		else:
			ans = a
	print ans