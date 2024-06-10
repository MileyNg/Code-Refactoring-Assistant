while True:
 a,op,b=raw_input().split()
 if op=="?":break
 if op=="+":print int(a)+int(b)
 if op=="-":print int(a)-int(b)
 if op=="*":print int(a)*int(b)
 if op=="/":print int(a)/int(b)