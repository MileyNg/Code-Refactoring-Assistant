def main():
    loop_count = 0
    while 1:
        loop_count += 1
        x = raw_input()
        if x == '0':
            break
        else:
            print 'Case %s: %s' %(loop_count ,x)

if __name__ == '__main__':
    main()