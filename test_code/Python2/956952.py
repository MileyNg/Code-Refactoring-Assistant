from collections import Counter

while 1:
    try:
        hand = map(int, raw_input().split(','))
    except EOFError:
        break
    count = Counter(hand).most_common()

    ret = ''
    if count[0][1] >= 4:
        ret = 'four card'
    elif len(count) >= 2 and count[0][1] == 3 and count[1][1] == 2:
        ret = 'full house'
    elif len(count) == 5:
        sort_hand = sorted(hand)
        for i in xrange(4):
            if sort_hand[i] + 1 != sort_hand[i + 1]:
                break
        else:
            ret = 'straight'
        if sort_hand == [1, 10, 11, 12, 13]:
            ret = 'straight'
    elif len(count) == 3 and count[0][1] == 3:
        ret = 'three card'
    elif len(count) == 3 and count[0][1] == count[1][1] == 2:
        ret = 'two pair'
    elif len(count) == 4:
        ret = 'one pair'
    if ret:
        print ret
    else:
        print 'null'