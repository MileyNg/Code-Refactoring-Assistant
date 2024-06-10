def main():  
    
    while 1:
        h,w = map(int,raw_input().split())
        if h+w == 0 : break
        
        for i in range(h):
            if i%2 == 0:
                print '#.'*(w/2) + '#'*(w%2)
            else:
                print '.#'*(w/2) + '.'*(w%2)
        print

if __name__ == '__main__':
    main()