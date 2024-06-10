A=[]
x=1.0
y=0.0
for i in range(1,1001):
    A.append([x,y])
    tmp=i**.5
    x,y=x-y/tmp,y+x/tmp

while 1:
    n=input()
    if n==-1:break
    a,b=A[n-1]
    print "%.2f\n%.2f"%(a,b)