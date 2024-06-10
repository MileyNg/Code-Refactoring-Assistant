def main():  
    
    a,b = map(int,raw_input().split())
    print '%d %d %.5f' %(a/b, a%b, a/float(b))

if __name__ == '__main__':
    main()