n = input()
mind = n
for i in range(max(0,n-100),min(10001,n+100)):
	if i == int(str(i)[::-1]) and abs(n - i) < mind:
		mind = abs(n - i)
		ans = i
print ans