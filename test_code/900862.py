from datetime import timedelta
def f(h,m,s):
    return timedelta(hours=h,minutes=m,seconds=s)

t1=f(2,0,0)
while 1:
    h,m,s=map(int,raw_input().split())
    if [h,m,s]==[-1,-1,-1]: break
    t=t1-f(h,m,s)
    t3=t*3
    print "0"+str(t)
    print "0"+str(t3)