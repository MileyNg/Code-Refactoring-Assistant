while 1:
	try:
		s,t = raw_input(),raw_input()
		if len(s) < len(t): s,t = t,s
		MAXL = sum(min(s.count(i),t.count(i)) for i in set(list(s))&set(list(t)))
		ans = 0
		for sp in range(len(t)):
			if len(t) - sp <= ans:
				break
			for L in range(ans+1,min(MAXL+1,len(t)-sp+1)):
				if t[sp:sp+L] in s:
					ans = L
				else:
					break
		print ans
	except:
		break