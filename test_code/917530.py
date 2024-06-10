n=input()
a=raw_input()
count=0
for r in range(n):
	b=raw_input()
	lb=len(b)
	flag=0
	for s in range(lb):
		for i in range(lb-(s+1)*(len(a)-1)):
			if b[i:i+(s+1)*len(a):s+1]==a:
				count+=1
				flag=1
				break
		if flag==1:break
print count
	