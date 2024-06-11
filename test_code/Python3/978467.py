while True:
    try:
       ban = input()
    except EOFError:
        break

    s = [ban[:3], ban[3:6], ban[6:]]
    s += map(''.join, zip(*s))
    s += [ban[0]+ban[4]+ban[8]] + [ban[2]+ban[4]+ban[6]]

    if 'ooo' in s:
        print('o')
    elif 'xxx' in s:
        print('x')
    else:
        print('d')