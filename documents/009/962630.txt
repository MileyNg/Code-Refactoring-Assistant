import math

def L(x1,y1,x2,y2):
  return math.sqrt((x1-x2)**2+(y1-y2)**2)

def S(a,b,c):
  s=(a+b+c)/2
  return math.sqrt(s*(s-a)*(s-b)*(s-c))

while True:
  try:
    x1,y1,x2,y2,x3,y3,xp,yp = map(float, raw_input().split())
    a  = L(x1,y1,x2,y2)
    b  = L(x1,y1,x3,y3)
    c  = L(x2,y2,x3,y3)
    pa = L(x3,y3,xp,yp)
    pb = L(x2,y2,xp,yp)
    pc = L(x1,y1,xp,yp)
    if S(a,pb,pc)+S(b,pc,pa)+S(c,pa,pb)-S(a,b,c) > 0.0000001:
      print "NO"
    else:
      print "YES"
  except:
    break