r = 2**15+1
sqrt = int(r**0.5)
p = [1]*(r+1)
p[:2] = [0,0]
for i in range(2,sqrt+1):
	if p[i]:
		p[2*i::i] = [0 for x in range(2*i,r+1,i)]
while 1:
	n = input()
	if n == 0: break
	count = 0
	for i in range(2,n/2+1):
		if p[i] and p[n-i]:
			count += 1
	print count