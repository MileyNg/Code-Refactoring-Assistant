while True:
    n = int(raw_input())
    if n == 0: break
    sm = 0
    while n != 0:
        n /= 5
        sm += n
    print sm