m=["NO","YES"]
for n in range(input()):
  a,b,c=sorted(map(int,raw_input().split()))
  print m[c*c==a*a+b*b]