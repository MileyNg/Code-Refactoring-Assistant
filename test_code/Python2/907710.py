def judge(exp,torf,i):
	if i==3:
		return eval(exp)
	else:
		return judge(exp,torf+[True],i+1) or judge(exp,torf+[False],i+1)
		
while 1:
	exp=raw_input().split("|")
	if exp[0]=="#":break
	for j in range(len(exp)):
		dic=[]
		exp[j]=list(exp[j])[1:-1]
		for i in range(len(exp[j])):
			if exp[j][i]=="&":exp[j][i]="and"
			elif exp[j][i]=="~":exp[j][i]="not"
			else:
				if exp[j][i] not in dic:
					dic.append(exp[j][i])
					exp[j][i]="torf["+str(len(dic)-1)+"]"
				else:
					exp[j][i]="torf["+str(dic.index(exp[j][i]))+"]"
		exp[j]=" ".join(map(str,exp[j]))
	for clause in exp:
		if judge(clause,[],0):
			print "yes"
			break
	else:
		print "no"