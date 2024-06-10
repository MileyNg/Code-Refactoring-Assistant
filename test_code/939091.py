def solve(n):
	if n > 0:
		for i in range(n,0,-1):
			if i <= ans[-1]:
				ans.append(i)
				solve(n-i)
				ans.pop()
	else:
		print ' '.join(map(str,ans[1:]))
while 1:
	n = input()
	if n==0: break
	ans = [n]
	solve(n)