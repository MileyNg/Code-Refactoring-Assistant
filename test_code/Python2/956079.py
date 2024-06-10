
while(True):
  n = input()
  if(n == 0):
    break
  a = 0
  b = 0
  for i in range(n):
    (l, r) = map(int, raw_input().split())
    if(l > r):
      a += l + r
    elif(l < r):
      b += l + r
    else:
      a += l
      b += r
  print "%d %d" % (a, b)
  