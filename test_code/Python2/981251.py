a,b,c=map(int,raw_input().split())
if(a>b):
 tmp=a
 a=b
 b=tmp
if(b>c):
 tmp=b
 b=c
 c=tmp
if(a>b):
 tmp=b
 b=a
 a=tmp
print str(a)+" "+str(b)+" "+str(c)