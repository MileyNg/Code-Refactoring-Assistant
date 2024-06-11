while True:
    h, w = map(int, input().strip().split())
    if h == w == 0: break
    print('#'*w + '\n' + ('#' + '.'*(w-2) + '#\n')*(h-2) + '#'*w + '\n')