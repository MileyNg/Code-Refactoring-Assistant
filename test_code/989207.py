def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

while(True):
    try:
        a = int(raw_input())
    except:
        break
    b = a
    
    while(True):
        b -= 1
        if(is_prime(b)):
            print b ,
            break

    while(True):
        a+=1
        if(is_prime(a)):
            print a
            break