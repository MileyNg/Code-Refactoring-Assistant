while True:
 m,f,r=map(int,raw_input().split())
 if m==-1 and f==-1 and r==-1:break
 if m+f<30 or m==-1 or f==-1:print "F"
 elif r>=50: print "C"
 elif m+f<50:print "D" 
 elif m+f<65: print "C" 
 elif m+f<80: print "B"
 elif 80<=m+f: print "A"