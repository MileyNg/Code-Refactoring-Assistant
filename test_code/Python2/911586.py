import sys
for s in sys.stdin:
  x1,y1,x2,y2,xq,yq =map(float,s[:-1].split(","))
  if x2==x1:
    y=yq
    x=x1
  else:
    m=1.0*(y2-y1)/(x2-x1)
    a=m*m+1
    x0=m*x1-y1
    y0=xq+m*yq
    x=(m*x0+y0)/a
    y=(-x0+m*y0)/a
  print "%0.5f %0.5f"%(2*x-xq,2*y-yq)