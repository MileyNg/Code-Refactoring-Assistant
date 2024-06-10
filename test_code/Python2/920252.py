a,b,c = raw_input().split()

while b != "?":
    if b == "+":
        print int(a) + int(c)
    elif b == "-":
        print int(a) - int(c)
    elif b == "*":
        print int(a) * int(c)
    elif b == "/":
        print int(a) / int(c)    
    a,b,c = raw_input().split()