#!/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function
try:
    input = raw_input
    range = xrange
except NameError:
    pass
# 上記のコードはPython2とPython3の違いを一部吸収するためのもの


def main():
    value = [0] * 1000
    weight = [0] * 1000
    casenum = 1
    while True:
        W = int(input())
        if(W == 0):
            return
        N = int(input())
        dp = [[0 for x in range(W+1)] for y in range(N+1)]
        for x in range(0, N):
            value[x], weight[x] = map(int, input().split(','))
        for i in range(0, N):
            for w in range(0, W+1):
                if w - weight[i] >= 0:
                    use = dp[i][w - weight[i]] + value[i]
                else:
                    use = 0
                unuse = dp[i][w]
                dp[i+1][w] = max(use, unuse)
        print("Case " + str(casenum) + ":")
        for w in range(W+1):
            if(dp[N][w] == dp[N][W]):
                print(str(dp[N][w]) + "\n" + str(w))
                break
        casenum += 1
main()