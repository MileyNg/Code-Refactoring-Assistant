while 1:
  c=[0,1,1]+[0]*98
  while 1:
    try: a, b = map(int, raw_input().split())
    except: exit()
    if a==0==b:break
    c[a] = -c[a]+1
    c[b] = -c[b]+1
  print ["NG","OK"][sum(c)==0]