while True:
	n = int(raw_input())
	if n == 0: break
	s = 32
	a = map(int, raw_input().split())
	i = 0
	while s > 0:
		s -= (s-1)%5
		print s
		s -= a[i%n] if s > a[i%n] else s
		print s
		i += 1