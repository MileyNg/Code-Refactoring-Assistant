R=range(8)
A=[4,1,4,1,2,1,2,1]
A+=A
B="41412121"
B=map(int,[B[i:]+B[:i] for i in R])

import sys
for s in sys.stdin:
  x=map(int,s[:-1].split())
  m=sum(x)
  for i in R:
    s=sum([max(0,x[j]-A[i+j]) for j in R])
    if s<m: m,p=s,i
    elif m==s and B[i]<B[p]: p=i
  for i in R: print A[p+i],
  print