n=input()
for i in range(n):
	x,y,b,p=map(int,raw_input().split())
	if b>4 and p>1:print (x*b+y*p)*8/10
	elif b>4:print min(x*b+y*p,(x*b+y*2)*8/10)
	elif p>1:print min(x*b+y*p,(x*5+y*p)*8/10)
	else:print min(x*b+y*p,(x*5+y*2)*8/10)