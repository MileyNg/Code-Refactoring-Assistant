import sys
s=0
i=0
for e in sys.stdin:
    ex,ey=map(float,e[:-1].split(","))
    if i==0:x0,y0=ex,ey
    elif i==1:x1,y1=ex-x0,ey-y0
    else: 
        x2,y2=ex-x0,ey-y0
        s+=abs(x1*y2-x2*y1)
        x1,y1=x2,y2
    i+=1
print s/2