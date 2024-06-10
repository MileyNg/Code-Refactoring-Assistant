import sys
for s in sys.stdin:
  y,m,d=map(int,s[:-1].split())
  x="%d%02d%02d"%(y,m,d)
  if x<"18680908":e="pre-meiji"
  elif x<"19120730":e="meiji %d %d %d"%(y-1867,m,d)
  elif x<"19261225":e="taisho %d %d %d"%(y-1911,m,d)
  elif x<"19890108":e="showa %d %d %d"%(y-1925,m,d)
  else:e="heisei %d %d %d"%(y-1988,m,d)
  print e