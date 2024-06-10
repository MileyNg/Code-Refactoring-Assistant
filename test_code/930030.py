try:
  while 1:
    c=[0,1,1]+[0]*98
    while 1:
      a, b = map(int, raw_input().split())
      if a==0==b:break
      c[a] = -c[a]+1
      c[b] = -c[b]+1
    if c.count(1): print "NG"
    else: print "OK"
except:exit