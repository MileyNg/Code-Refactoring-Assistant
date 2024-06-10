import sys,cmath,math
c=[]
for s in sys.stdin:
    x,y=map(float,s[:-1].split(","))
    c+=[complex(x,y)]
c0=c[0]
c1=c[1]
r1,a1=cmath.polar(c1-c0)
s=0
for e in c[2:]:
    r2,a2=cmath.polar(e-c0)
    s+=r1*r2*math.sin(abs(a1-a2))/2
    r1,a1=r2,a2
print s