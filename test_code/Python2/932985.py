import math,cmath
e=1e-6
def f(m):
  c=1j*math.acos(a/2)
  p1=cmath.exp(b+c)+p
  p2=cmath.exp(b-c)+p
  s1,s2=2,2
  for p3 in X:
    if p3 in[p,p0]:continue
    if abs(p3-p1)<1+e:s1+=1
    if abs(p3-p2)<1+e:s2+=1
  return max(m,s1,s2)

while 1:
  n=input()
  if n==0:break
  N=range(n)
  X=[]
  for i in N:
    x,y=map(float,input())
    X+=[x+1j*y]
  m=1
  for i in N:
    p=X[i]
    for p0 in X[i+1:]:
      a,b=cmath.polar(p0-p)
      b*=1j
      if a<=2:m=f(m)
  print m