while True:
 n,x=map(int,raw_input().split())
 if n==0 and x==0:break
 count=0
 for i in range(1,n+1):
  for j in range(i+1,n+1):
   for k in range(j+1,n+1):
    
    if i+j+k==x:
	 count+=1	 
 print count