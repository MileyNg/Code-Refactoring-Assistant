from math import pi
r, = map(float, raw_input().split())
area = r**2*pi
length = 2*r*pi
print "%f %f"%(area, length)