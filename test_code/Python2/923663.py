#coding:utf-8

from __future__ import division, print_function
try:
    input = raw_input
    range = xrange
except NameError:
    pass


def solve(cnt, W, N, treasures):
    dp = [0] + [-1] * W
    for v, w in treasures:
        for j in range(W, w - 1, -1):
            if dp[j - w] >= 0:
                dp[j] = max(dp[j], dp[j - w] + v)

    ans = max(dp)
    print('Case %d:\n%d\n%d' % (cnt, ans, dp.index(ans)))

cnt = 1
while True:
    W = int(input())
    if W == 0:
        break
    N = int(input())
    
    treasures = [tuple(map(int, input().split(','))) for _ in range(N)]
    solve(cnt, W, N, treasures)

    cnt += 1