import math
n = int(raw_input())
a = 100000
for i in range(n):
    a = int(math.ceil(a * 0.00105)) * 1000
print a