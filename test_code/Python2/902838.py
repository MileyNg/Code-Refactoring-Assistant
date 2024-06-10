dp = [[0] * 4001 for _ in range(4)]
for i in range(1001):
    dp[0][i] = 1
for i in range(1, 4):
    for j in range((i + 1) * 1000 + 1):
        dp[i][j] += sum(dp[i - 1][max(0, j - 1000): j + 1])

while 1:
    try:
        print dp[3][input()]
    except:
        break