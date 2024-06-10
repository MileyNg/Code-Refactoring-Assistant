import sys
c=[map(float,s[:-1].split(",")) for s in sys.stdin]
x0,y0=c[0]
x1,y1=c[1][0]-x0,c[1][1]-y0
s=0
for ex,ey in c[2:]:
    x2,y2=ex-x0,ey-y0
    s+=abs(x1*y2-x2*y1)
    x1,y1=x2,y2
print s/2