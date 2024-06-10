def solve(a,M):
	for x,y in xy:
		if x in a and (y not in a or a.index(x) > a.index(y)): break
	else:
		if len(a) == m: return a
		for i in range(len(M)):
			r =  solve([M[i]] + a,M[:i]+M[i+1:])
			if r: return r
m = input()
xy = [map(int,raw_input().split()) for i in range(input())]
for i in solve([],range(1,m+1)): print i