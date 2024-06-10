while 1:
    x=input()
    h=input()
    if [x,h]==[0,0]:break
    a=float(x)/2
    s=((a*a+h*h)**0.5*2+x)*x
    print s