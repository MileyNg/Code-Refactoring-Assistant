while 1:
    try:
        numbers = map(int, raw_input())
    except EOFError:
        break
    dp = [[0] * 10 for _ in xrange(10)]
    dp[0] = numbers
    for i in xrange(9):
        for j in xrange(len(dp[i]) - 1):
            dp[i + 1][j] = (dp[i][j] + dp[i][j + 1]) % 10
    print dp[-1][0]