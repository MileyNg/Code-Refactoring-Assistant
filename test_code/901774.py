N=60
def f(t):
    c,t=t%N,t/N
    print "%02d:%02d:%02d"%(t/N,t%N,c)
    return

while 1:
    h,m,s=map(int,raw_input().split())
    if [h,m,s]==[-1,-1,-1]: break
    t=7200-(h*N+m)*N-s
    f(t)
    f(t*3)