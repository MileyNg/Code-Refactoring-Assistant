while True:
 x,y=map(int,raw_input().split())
 if x==0 and y==0:break
 if x>y:
  tmp=x
  x=y
  y=tmp
 print str(x)+" "+str(y)