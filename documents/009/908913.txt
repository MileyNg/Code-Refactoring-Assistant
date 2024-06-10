import sys
count={}
for line in sys.stdin.readlines():
	n=int(line.rstrip())
	if not count.has_key(n):
		count[n]=0
	count[n]+=1

max=max(count.values())
for k,v in sorted(count.items()):
	if v==max:
		print k