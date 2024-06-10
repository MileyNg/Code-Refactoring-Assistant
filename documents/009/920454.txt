import sys

def comb(sum,c,s):
	if c>1:
		val=0
		for i in range(s,10):
			if sum-i>0:
				val+=comb(sum-i,c-1,i+1);
		return val
	else:
		return 1 if sum>=s and sum<10 else 0

while True:
	c,sum=map(int,raw_input().split(" "))
	if c:
		print comb(sum,c,0)
	else:
		break