import sys
for s in sys.stdin:
    n,w,h=s.split(",")
    n,w,h=int(n),float(w),float(h)
    bmi=w/h/h
    if bmi>=25: print n