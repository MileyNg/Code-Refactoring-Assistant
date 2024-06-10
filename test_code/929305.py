import sys
for s in sys.stdin:
  n,m=map(int,s.split())
  if n==0&m==0:break
  G=range(1,n+1)
  while n>1:
    if m%n==0:G=G[:n-1]
    else:G=G[m%n:]+G[:(m-1)%n]
    n-=1
  print G[0]