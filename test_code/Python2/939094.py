def f(a,n):
	for i in range(min(n,a[-1]),0,-1): f(a+[i],n-i)
	if n == 0: print " ".join(map(str,a[1:]))
while 1:
	n = input()
	if n==0: break
	f([n],n)