import sys
for s in sys.stdin:
  y,m,d=map(int,s[:-1].split())
  x="%d%02d%02d"%(y,m,d)
  w=" %d %d"%(m,d)
  if x<"18680908":e="pre-meiji"
  elif x<"19120730":e="meiji %d"%(y-1867)+w
  elif x<"19261225":e="taisho %d"%(y-1911)+w
  elif x<"19890108":e="showa %d"%(y-1925)+w
  else:e="heisei %d"%(y-1988)+w
  print e