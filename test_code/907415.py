import sys
x=[map(float,s[:-1].split(",")) for s in sys.stdin]
s=[x[i][0]*x[i-1][1]-x[i][1]*x[i-1][0] for i in range(len(x))]
print abs(sum(s))/2