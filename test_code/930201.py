import sys
buf=[]
op="+-*/"
def f(i):
  b=buf.pop()
  a=buf.pop()
  if i==0:x=a+b
  elif i==1:x=a-b
  elif i==2:x=a*b
  else:x=a/b
  buf.append(x)
  return
for s in sys.stdin:
  for e in s.split():
    if op.count(e):f(op.index(e))
    else:buf.append(float(e))
  print buf.pop()