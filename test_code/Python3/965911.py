from collections import Counter
import sys

for line in sys.stdin:
    card = sorted(list(map(int, line.split(','))))
    pair = Counter(card).most_common()

    if pair[0][1] == 4:
        print('four card')
    elif pair[0][1] == 3 and pair[1][1] == 2:
        print('full house')
    elif pair[0][1] == 3:
        print('three card')
    elif pair[0][1] == pair[1][1] == 2:
        print('two pair')
    elif pair[0][1] == 2:
        print('one pair')
    elif [x - card[0] for x in card] == [0,1,2,3,4] or card == [1,10,11,12,13]:
        print('straight')
    else:
        print('null')