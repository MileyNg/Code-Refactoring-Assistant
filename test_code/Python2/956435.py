while 1:
	n = input()
	if n == 0: break
	a = map(int,raw_input().split())
	da = [a[i+1] - a[i] for i in range(n)]
	d = sorted(list(set(da)), key = lambda x:da.count(x))[-1]
	for i in range(n):
		if i == 0 and a[i] + d != a[i+1]:
			if a[i+1] + d != a[i+2]:
				print a[i+1]
			else:
				print a[i]
			break
		elif a[i] + d != a[i+1]:
			print a[i+1]
			break