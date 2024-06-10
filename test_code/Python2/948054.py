ans = 100000
n = int(raw_input())
for i in xrange(n):
	ans *= 1.05
	ans = int((ans+999)/1000)*1000;
print ans