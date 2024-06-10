for _ in range(input()):
	n,k = map(int,raw_input().split())
	x = map(int,raw_input().split())
	d = [x[i+1]-x[i] for i in range(n-1)]
	print x[-1] - x[0] - sum(sorted(d)[::-1][:k-1])