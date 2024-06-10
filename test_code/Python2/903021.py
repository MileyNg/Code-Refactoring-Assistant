from fractions import gcd
n=input()
L=map(int,raw_input().split())
g=reduce(gcd,L)
for i in range(1,g+1):
    if g%i==0:print i