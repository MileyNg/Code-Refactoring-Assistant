while True:
    H, W = map(int, raw_input().split())
    if 0 <= H <= W <= 0:
        break
    print "\n".join("#" * W for _ in xrange(H)) + "\n"