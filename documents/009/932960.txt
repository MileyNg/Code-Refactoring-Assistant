import math,cmath
e=1e-6
j=1j
def f(m):
  c=j*math.acos(a/2)
  p1=cmath.exp(b+c)+p0
  p2=cmath.exp(b-c)+p0
  s1,s2=2,2
  for k in N:
    if k==i or k==i1:continue
    if abs(X[k]-p1)<1+e:s1+=1
    if abs(X[k]-p2)<1+e:s2+=1
  return max(m,s1,s2)

while 1:
  n=input()
  if n==0:break
  N=range(n)
  X=[]
  for i in N:
    x,y=map(float,input())
    X+=[x+j*y]
  m=1
  for i in N:
    p0=X[i]
    for i1 in range(i+1,n):
      p=X[i1]-p0
      a,b=cmath.polar(p)
      b*=j
      if a<=2:m=f(m)
  print m