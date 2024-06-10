def delta(t1,t2):
    h,m = [int(t2[i:i+2]) - int(t1[i:i+2]) for i in [0,3]]
    return 60*h + m
     
n,t = map(int,raw_input().split())
s = [raw_input().split() for i in range(n)]
a = []
for i in range(1,n):
    dt = delta(s[i-1][2],s[i][0])
    if dt >= t:
        a.append([s[i][1],str(dt)])
print len(a)
for i in a:
    print " ".join(i)