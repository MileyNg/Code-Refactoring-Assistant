while 1:
  q=input()
  if q==-1: break
  x=q/2.0
  while 1:
    a=x**3-q
    if abs(a)<1e-5*q: break
    x-=a/3/x/x
  print x