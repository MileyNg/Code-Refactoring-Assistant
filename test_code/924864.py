import sys

def drange(start, stop, step):
  r = start
  while r <= stop:
    yield r
    r += step

for s in sys.stdin:
  d = int(s)
  sum = 0
  for x in drange(d, 600, d):
    sum += (x-d)**2*d
  print '%d'%sum