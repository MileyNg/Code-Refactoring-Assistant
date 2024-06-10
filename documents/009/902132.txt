while 1:
    cards = raw_input()
    if cards == '-':
        break
    for i in range(input()):
        h = input()
        cards = cards[h:] + cards[:h]
    print cards