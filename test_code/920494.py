import sys

for line in sys.stdin:
	l=map(int,line.split(','))
	v=l[-2:]
	del l[-2:]

	al=0
	for i in l:
		al+=i
	al=v[0]*al/float(v[0]+v[1])

	for i in range(10):
		al-=l[i]
		if al<=0:
			print i+1
			break