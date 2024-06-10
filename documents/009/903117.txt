if __name__ == '__main__':
    output = []
    while True:
        x, y = map(int, raw_input().split(' '))
        if x == 0 and y == 0:
            break
        else:
            if x > y:
                output.append('%d %d' % (y, x))
            else:
                output.append('%d %d' % (x, y))

    for line in output:
        print line