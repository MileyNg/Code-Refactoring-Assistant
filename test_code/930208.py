import sys
def f(b,a,e):
  if e=="+":x=a+b
  elif e=="-":x=a-b
  elif e=="*":x=a*b
  else:x=a/b
  return x
for s in sys.stdin:
  A=[]
  for e in s.split():
    try:x=float(e)
    except:x=f(A.pop(),A.pop(),e)
    A+=[x]
  print A[0]