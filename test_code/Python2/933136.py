def fact(n):
	return 1 if n == 0 else n*fact(n-1)

S = raw_input()
l,s = len(S),set(list(S))
lens = len(s)
d = [S.count(i) for i in s]
if l%2 == 0:
	for i in range(lens):
		if d[i]%2 == 1:
			print 0
			break
	else:
		denomi = 1
		for i in range(lens):
			denomi *= fact(d[i]/2)
		print fact(l/2)/denomi
else:
	for i in range(lens):
		if sum([d[i]%2 for i in range(lens)]) != 1:
			print 0
			break
	else:
		denomi = 1
		for i in range(lens):
			denomi *= fact(d[i]/2) if d[i]%2 == 0 else fact((d[i]-1)/2)
		print fact((l-1)/2)/denomi