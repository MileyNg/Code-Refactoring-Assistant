count={}
for s in raw_input().rstrip().split():
	if not count.has_key(s):
		count[s]=[len(s),0]
	count[s][1]+=1

long,mode=max([x[0] for x in count.values()]),max([x[1] for x in count.values()])
for k,v in count.items():
	if v[0]==long:
		long=k
	if v[1]==mode:
		mode=k

print mode,long