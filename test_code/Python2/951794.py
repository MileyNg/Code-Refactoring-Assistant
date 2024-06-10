import itertools
while 1:
	n = input()
	if n == 0: break
	k = input()
	C = [input() for i in range(n)]
	ans = set()
	for c in itertools.permutations(C,k):
		ans.add("".join(map(str,c)))
	print len(ans)