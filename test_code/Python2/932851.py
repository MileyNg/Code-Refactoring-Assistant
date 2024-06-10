steps=[1,2,4]+ [0]*27
for i in range(3,30):
  steps[i]=steps[i-1]+steps[i-2]+steps[i-3]
while True:
  n=input()
  if n==0:break
  print steps[n-1]/10/365+1