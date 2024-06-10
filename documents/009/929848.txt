S = 0
for i in range(input()):
	p,x = raw_input().split()
	x = int(x)
	S += x if p == "(" else -x
	if S < 0:
		break
print "YES" if S == 0 else "NO"