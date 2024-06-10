while 1:
  n,m=map(int,raw_input().split())
  if n==0==m:break
  G=range(1,n+1)
  p=0
  while n>1:
    p=(p+m-1)%n
    G.pop(p)
    n-=1
  print G[0]