#coding:utf-8
from __future__ import division,print_function
try:
    input = raw_input
except NameError:
    pass
# 上記のコードはPython2とPython3の違いを一部吸収するためのもの

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


def solve(numbers):
    MAX_NUMBER = 20
    SIGN = [-1,+1]
    rightside_of_expression = numbers[-1]
    leftside_of_expession = numbers[:-1]

    # (N-1) * 21 の表
    #  way_to_make[i][j] = i項まで使ってjをつくる+/-の組み合わせ
    way_to_make = make_matrix(len(leftside_of_expession),MAX_NUMBER+1,0)

    # インデックスを使いたいので直接 for i in leftside_of_expessionとはしない。
    #  enumerateをつかっても良い
    for i in range(len(leftside_of_expession)):
        v = leftside_of_expession[i]
        # 最初の項は+しかない。
        if i == 0:
            way_to_make[0][v] = 1
        else:
            for j in range(MAX_NUMBER+1):
                # way_to_make[i][j] = way_to_make[i-1][j-numbers[i]]
                #                   + way_to_make[i-1][j+numbers[i]]
                for s in SIGN:
                    p = j + s*numbers[i]
                    if 0 <= p <= MAX_NUMBER:
                        way_to_make[i][j] += way_to_make[i-1][p]

    return way_to_make[-1][rightside_of_expression]

def main():
    N = int(input())

    string_of_numbers = input().split(" ")
    numbers = []
    for s in string_of_numbers:
        numbers.append(int(s))

    # solveはNを必要としない。(N = len(numbers)だから。)
    print(solve(numbers))

main()