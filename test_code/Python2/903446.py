import sys
for s in sys.stdin:
    n,w,h=map(float, s.split(","))
    bmi=w/h/h
    if bmi>=25: print int(n)