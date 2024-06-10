def main():  
    
    while 1:
        a,op,b = raw_input().split()
        a = int(a)
        b = int(b)
        
        if op == '+': a += b
        elif op == '-': a -= b
        elif op == '*': a *= b
        elif op == '/': a /= b
        elif op == '?': break
        print a

if __name__ == '__main__':
    main()