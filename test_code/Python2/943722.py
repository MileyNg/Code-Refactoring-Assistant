while 1:
	inp = raw_input()
	if inp == ".": break
	a = ""
	for i in inp:
		if i == "(" or i == ")" or i == "[" or i == "]":
			a += i
	while len(a) > 0:
		if   "()" in a: a = a.replace("()","")
		elif "[]" in a: a = a.replace("[]","")
		else: break
	print "yes" if len(a) == 0 else "no"