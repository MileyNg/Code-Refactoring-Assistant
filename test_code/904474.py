N=1001
A=[[]]*N
x=1.0
y=0.0
for i in range(1,N):
    A[i]=[x,y]
    tmp=i**.5
    x,y=x-y/tmp,y+x/tmp
 
while 1:
    n = input()
    if n==-1:break
    a,b=A[n]
    print a,b