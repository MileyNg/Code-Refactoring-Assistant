from collections import Counter

while 1:
    try:
        puzzle = map(int, raw_input())
    except EOFError:
        break
    ret = []
    for i in xrange(1, 10):
        cnt = Counter(puzzle + [i])
        if cnt[i] > 4:
            continue
        for j in xrange(1, 10):
            if cnt[j] < 2:
                continue
            tmp = Counter(puzzle + [i])
            tmp[j] -= 2
            for k in xrange(1, 10):
                if not tmp[k]:
                    continue
                if tmp[k] >= 3:
                    tmp[k] -= 3

                while tmp[k] and tmp[k + 1] and tmp[k + 2]:
                    tmp[k] -= 1
                    tmp[k + 1] -= 1
                    tmp[k + 2] -= 1
                if tmp[k]:
                    break
            else:
                ret.append(i)
                break
    if ret:
        print ' '.join(map(str, ret))
    else:
        print 0