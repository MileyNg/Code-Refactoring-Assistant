N,M = map(int,raw_input().split())
ab = [map(int,raw_input().split()) for i in range(M)]
maxb = 0
for a,b in ab:
	if a == 1 and b > maxb:
		maxb = b
flag = 0 if maxb > 0 else 1
i = 1
while maxb < N and flag == 0:
	lsb = [b for a,b in ab if a <= maxb + 1 and b > maxb]
	if len(lsb) > 0:
		maxb = max(lsb)
	else:
		flag = 1
	i += 1
print i if maxb == N and flag == 0 else "Impossible"
	