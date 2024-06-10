while True:                
    x = input().strip()    
    if x == '0': break     
    print(sum(map(int, x)))