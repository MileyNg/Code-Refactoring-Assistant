time=input()
h=time/3600
time=time%3600
m=time/60
time=time%60
s=time
print str(h)+":"+str(m)+":"+str(s)