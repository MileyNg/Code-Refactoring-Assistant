rank = [0, 48, 51, 54, 57, 60, 64, 69, 75, 81, 91, 1 << 30]
rank_name = ['light fly',
             'fly',
             'bantam',
             'feather',
             'light',
             'light welter',
             'welter',
             'light middle',
             'middle',
             'light heavy',
             'heavy', ]

while 1:
    try:
        weight = input()
        for i in xrange(len(rank_name)):
            if rank[i] < weight <= rank[i + 1]:
                print rank_name[i]
                break
    except EOFError:
        break