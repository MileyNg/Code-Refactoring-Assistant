while 1:
	n,k = map(int,raw_input().split())
	s = [0]*(n+1)
	if n == 0: break
	c = sorted([int(raw_input()) for i in range(k)])
	have0 = 1 if c[0] == 0 else 0
	jump = 0
	for i in c[have0:]:
		s[i] = s[i-1] + 1
		if have0 and s[i-1] == 0 and s[i-2] > 0:
			s[i] += s[i-2] + 1 - jump
			jump = s[i-2] + 1
		if s[i-1] == 0 and s[i-2] == 0:
			jump = 0
	print max(s)