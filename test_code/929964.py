while 1:
  n,m=map(int,raw_input().split())
  if n==0==m:break
  p=0
  for i in range(2,n+1):p=(p+m)%i
  print p+1