import sys
x0,y0=map(float,raw_input()[:-1].split(","))
x1,y1=map(float,raw_input()[:-1].split(","))
x1,y1=x1-x0,y1-y0
s=0
for e in sys.stdin:
    ex,ey=map(float,e[:-1].split(","))
    x2,y2=ex-x0,ey-y0
    s+=abs(x1*y2-x2*y1)
    x1,y1=x2,y2
print s/2