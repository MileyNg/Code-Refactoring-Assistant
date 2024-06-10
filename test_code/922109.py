import sys
for s in sys.stdin:
  y,m,d=map(int,s[:-1].split())
  x=y*10000+m*100+d
  def f(i,w):
    print ["meiji","taisho","showa","heisei"][i],y-w,m,d
  if x<18680908:print"pre-meiji"
  elif x<19120730:f(0,1867)
  elif x<19261225:f(1,1911)
  elif x<19890108:f(2,1925)
  else:f(3,1988)