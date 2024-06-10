import math

a, b, t = map(int, input().strip().split())

t = math.radians(t)
h = b * math.sin(t)
l = a + b + math.sqrt(a*a + b*b - 2*a*b*math.cos(t))
s = a * h / 2
print(s)
print(l)
print(h)