r = 1000000
sqrt = int(r**0.5)
p = [1]*r
p[0] = 0
p[3::2] = [0 for x in range(3,r,2)]
for i in range(2,sqrt):
	if p[i]:
		p[2*i+1::i+1] = [0 for x in range(2*i+1,r,i+1)]

while 1:
	n = int(raw_input())
	if n == 0: break
	ans = 0
	for i in range(2,n/2+1):
		if p[i-1] and p[n-i-1]:
			ans += 1
	print ans