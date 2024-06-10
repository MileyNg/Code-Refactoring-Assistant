import sys

for s in sys.stdin:
  nb = format(int(s), 'b')
  arr = list(reversed(nb))
  ans = []
  i = 0
  for a in arr:
    if a == '1':
      ans.append(str(2**i))
    i += 1
  print ' '.join(ans)