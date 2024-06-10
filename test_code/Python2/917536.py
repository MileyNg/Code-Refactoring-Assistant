n=input()
a=raw_input()
la=len(a)
count=0
for r in range(n):
	b=raw_input()
	lb=len(b)
	flag=0
	for skip in range(lb):
		for ini in range(lb-(skip+1)*(la-1)):
			if b[ini:ini+(skip+1)*la:skip+1]==a:
				count+=1
				flag=1
				break
		if flag==1:break
print count
	