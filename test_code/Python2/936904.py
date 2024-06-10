while True:
  (x, y) = map(int, raw_input().split())
  if x==0 and y==0:
    break
  if x > y:
    print "%d %d" % (y, x)
  else:
    print "%d %d" % (x, y)