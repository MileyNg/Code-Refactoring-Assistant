while 1:
    n = int(raw_input())
    if n == 0:
        break
    A = [0] * n
    for i in xrange(n):
        A[i] = int(raw_input())
    for i in xrange(1, len(A)):
        A[i] = max(A[i - 1] + A[i], A[i])
    print max(A)