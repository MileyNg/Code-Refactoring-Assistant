while 1:
    H, W = map(int,raw_input().split())
    if H + W == 0: break
    print ('#' * W)
    for h in range(H-2):
        print ('#' + '.' * (W - 2) + '#')
    print ('#' * W + '\n')