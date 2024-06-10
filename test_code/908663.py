import sys

lists=[]
for str in sys.stdin:
	lists+=[tuple(str.rstrip().split(' '))]

for i in range(0,len(lists),2):
	hit=0
	blow=0
	for j in range(4):
		if lists[i][j]==lists[i+1][j]:
			hit+=1
	for c in lists[i]:
		if c in lists[i+1]:
			blow+=1
	print '%d %d' % (hit,blow-hit)