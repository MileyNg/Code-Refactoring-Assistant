
while 1:
    n = input()
    if n == 0:
        break
    A = []
    for i in xrange(n):
        A.append(int(raw_input()))
    dp = [0] * len(A)
    dp[0] = A[0]
    for i in xrange(1, len(A)):
        dp[i] = max(dp[i - 1] + A[i], A[i])
    print max(dp)