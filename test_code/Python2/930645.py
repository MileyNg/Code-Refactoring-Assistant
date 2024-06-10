import sys
x=[]
for s in sys.stdin:
  A=map(int,s[:-1].split(','))
  n=len(A)
  if len(x)<n: x=[0]+x+[0]
  x=[max(x[i:i+2])+A[i] for i in range(n)]
print x[0]