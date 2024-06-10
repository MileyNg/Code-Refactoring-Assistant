if __name__ == '__main__':

    numbers = []

    while True:
        x = int(raw_input())
        if x == 0:
            break
        numbers.append(x)

    i = 1

    for n in numbers:
        print 'Case %d: %d' % (i, n)
        i += 1