import sys
for s in sys.stdin:
    n,w,h=map(float,s.split(","))
    n=int(n)
    bmi=w/h/h
    if bmi>=25: print n