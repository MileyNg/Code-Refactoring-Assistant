#coding:utf-8
from __future__ import division,print_function
try:
    input = raw_input
    range = xrange
except NameError:
    pass
# 上記のコードはPython2とPython3の違いを一部吸収するためのもの

# http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=916014

# N * Mの表をつくる.すべての要素はvにする。
def make_matrix(N,M,v):
    # return [[v for i in range(M)] for j in range(N)]とも書ける。
    ret = []
    for i in range(N):
        l = []
        for j in range(M):
            l.append(v)
        ret.append(l)
    return ret


# gは行列(二次元配列)
def solve(n,m,g):
    # current_max[i][j] = 直前がjの場合のi日目の最大成長度
    # 負の数にはなりえない。
    current_max = make_matrix(m,n,-1)
    # 最初は何をあげても1.0のまま
    for i in range(n):
        current_max[0][i] = 1.0
    for i in range(1,m):
        # jは次にあげるもの
        for j in range(n):
            # 前に何をあげてたか
            # current_max[i][j] = max(current_max[i-1][k] * g[k][j]) for k in [0,n]
            for k in range(n):
                current_max[i][j] = max(current_max[i][j],
                                        current_max[i-1][k]*g[k][j])
    ret = max(current_max[m-1])
    ret = round(ret,2)
    print("%.2f" % ret)

def main():
    while True:
        # 受けとった文字列をintに変換する(リストの内包表記)
        n,m = [int(i) for i in input().split(" ")]
        if n == 0 and m == 0:
            return
        g = []
        for i in range(n):
            g.append([float(x) for x in input().split(" ")])

        solve(n,m,g)
main()