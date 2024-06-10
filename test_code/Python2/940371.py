def solve(a):
	for i in M-set(a):
		if any(x == i and y not in a for x,y in xy): continue
		r = solve([i]+a)
		if r: return r
	return a
m = input()
M = set(range(1,m+1))
xy = [map(int,raw_input().split()) for i in range(input())]
for i in solve([]): print i