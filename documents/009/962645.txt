import math

a, b, C = map(float, input().strip().split())
h = b * math.sin(math.radians(C))
print(a * h / 2)
print(a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C))))
print(h)