r = 10001
sqrt = int(r**0.5)
p = [1]*r
p[0] = 0
for i in range(1,sqrt):
	if p[i]:
		p[2*i+1::i+1] = [0 for x in range(2*i+1,r,i+1)]

while True:
	n = int(raw_input())
	if n == 0: break
	for i in range(n,1,-1):
		if p[i-1] and p[i-3]:
			print i-2,i
			break