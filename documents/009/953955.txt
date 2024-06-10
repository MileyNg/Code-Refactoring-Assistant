r = 100001
p = [1]*r
p[0] = p[1] = 0
for i in range(int(r**0.5)):
	if p[i]:
		p[2*i::i] = [0 for x in range(2*i,r,i)]
prime = []
for i in range(r):
	if p[i]: prime.append(i)
	
while 1:
	n = int(raw_input())
	if n == 0: break
	ans = 0
	i = 0
	while 1:
		s = 0
		j = i
		while 1:
			s += prime[j]
			if s >= n:
				if s == n:
					ans += 1
				break
			j += 1
		i += 1
		if prime[i] > n: break
	print ans