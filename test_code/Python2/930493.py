import math
while True:
	n = int(raw_input())
	if n==0:
		break
	s = map(int,raw_input().split())
	ave = sum = 0.0
	for i in xrange(n):
		ave += s[i]
	ave /= n
	for i in xrange(n):
		sum += math.pow(s[i] - ave, 2.0)
	print math.sqrt(sum/n)
	