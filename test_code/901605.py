r = 10001
sqrt = int(r**0.5)
p = [1]*r
twin = [0]*r
p[0] = 0
p[1::2] = [0 for x in range(1,r,2)]
for i in range(2,r,2):
	if p[i]:
		p[2*i+1::i+1] = [0 for x in range(2*i+1,r,i+1)]
		if p[i-2]:
			twin[i:i+250] = [i+1 for x in range(i,i+250)]
		
while True:
	n = int(raw_input())
	if n == 0: break
	print twin[n-1]-2,twin[n-1]