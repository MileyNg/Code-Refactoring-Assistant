import math
 
a,b,C = map(float,raw_input().split())
C = C / 180.0 * math.pi

S = a * b * math.sin(C) / 2.0
L = math.sqrt(pow(b * math.sin(C), 2) + pow(a - b * math.cos(C), 2)) + a + b
h = b * math.sin(C)

print "%f\n%f\n%f\n" % (S,L,h)