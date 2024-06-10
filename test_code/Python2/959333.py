# coding:utf-8

if __name__ == "__main__":
    while 1:
        x = map(int, raw_input().split())
        a = x[0]
        b = x[1]
        if a == 0 and b == 0:
            break
        if a >= b:
            print "%d %d" % (b, a)
        else:
            print "%d %d" % (a, b)