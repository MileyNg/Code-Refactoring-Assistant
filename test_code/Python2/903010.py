k=l=m=n=0
while 1:
	a,b,c=sorted(map(int,raw_input().split()))
	if a+b<=c:break
	k+=1
	if a**2+b**2>c**2:m+=1
	elif a**2+b**2<c**2:n+=1
	else:l+=1
print k,l,m,n