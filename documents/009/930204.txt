import sys
A=[]
def f(b,a,i):
  if i==0:x=a+b
  elif i==1:x=a-b
  elif i==2:x=a*b
  else:x=a/b
  return x
for s in sys.stdin:
  for e in s.split():
    try:A+=[float(e)]
    except:A+=[f(A.pop(),A.pop(),"+-*/".index(e))]
  print A.pop()