A=[]
x=1.0
y=0.0
for i in range(1001):
    A.append([x,y])
    tmp=(x**2+y**2)**.5
    dx,dy=-y/tmp,x/tmp
    x+=dx
    y+=dy

while 1:
    n=input()
    if n==-1:break
    a,b=A[n-1]
    print "%.2f\n%.2f"%(a,b)