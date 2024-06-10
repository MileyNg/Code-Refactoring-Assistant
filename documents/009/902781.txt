while 1:
    try:
        A = map(int, raw_input().split())
        B = map(int, raw_input().split())
        hit = sum(1 for i in range(4) if A[i] == B[i])
        blow = len(set(A) & set(B)) - hit
        print hit, blow
    except:
        break