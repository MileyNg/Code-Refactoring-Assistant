def main():  
    
    while 1:
        h,w = map(int,raw_input().split())
        if h+w == 0 : break
        for i in range(h):
            print '#'*w
        print

if __name__ == '__main__':
    main()