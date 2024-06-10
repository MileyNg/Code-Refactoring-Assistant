upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = "abcdefghijklmnopqrstuvwxyz"

while 1:
	a,type = raw_input().split()
	if type == "X": break
	ans = ""
	if type == "U":
		if "_" in a:
			words = a.split("_")
			for word in words:
				ans += upp[low.index(word[0])] + word[1:]
		else:
			ans = upp[low.index(a[0])] + a[1:] if a[0] in low else a
	elif type == "L":
		if "_" in a:
			words = a.split("_")
			ans += words[0]
			for word in words[1:]:
				ans += upp[low.index(word[0])] + word[1:]
		else:
			ans = low[upp.index(a[0])] + a[1:] if a[0] in upp else a
	else:
		if "_" not in a:
			words = []
			sp = 0
			for i in range(1,len(a)):
				if a[i] in upp:
					words.append(a[sp:i].lower())
					sp = i
			words.append(a[sp:].lower())
			ans = "_".join(words)
		else:
			ans = a
	print ans