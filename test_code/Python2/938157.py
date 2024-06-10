import itertools
while 1:
	n = input()
	if n == 0: break
	a = map(int,raw_input().split())
	all = sum(a)
	ans = all
	for i in range((n+1)/2+1):
		for party in itertools.combinations(a,i):
			ans = min(ans,abs(all-2*sum(party)))
	print ans