import bisect
try:
    while True:
        a = map(int, raw_input().split(','))
        b = [0] * 11
        for i in range(10):
            b[i + 1] = b[i] + a[i]
        print bisect.bisect_left(b, float(a[-2]) * b[-1] / (a[-1] + a[-2]))
except:
    pass