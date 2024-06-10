while 1:
	n=input()
	if n==0:break
	p=raw_input().split()+["end"]
	sp=p[0]
	ans=[]
	for i in range(n):
		if str(int(p[i])+1)!=p[i+1]:
			if sp!=p[i]:
				ans.append(sp+"-"+p[i])
			else:
				ans.append(sp)
			sp=p[i+1]
	print " ".join(ans)