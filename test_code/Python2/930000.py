while 1:
  try:
    c = [0]*101
    while 1:
      a, b = map(int, raw_input().split())
      if a==0==b:break
      c[a] += 1
      c[b] += 1
    c = map(lambda x: x%2, c)
    if c[1] and c[2] and sum(c[3:])==0:print"OK"
    else:print"NG"
  except:break