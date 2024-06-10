for n in range(input()):
  a,b,c=sorted(map(int,raw_input().split()))
  print ["NO","YES"][c*c-a*a-b*b==0]