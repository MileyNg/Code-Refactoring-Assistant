import sys
for s in sys.stdin:
    a,b,c=s.split(",")
    n=int(a)
    w,h=map(float,[b,c])
    bmi=w/h/h
    if bmi>=25: print n