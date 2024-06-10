#coding:utf-8
from __future__ import division,print_function
try:
    input = raw_input
except NameError:
    pass
# 上記のコードはPython2とPython3の違いを一部吸収するためのもの
memo=[0]*31
def solve(x):
    if memo[x]==0:
        if x>0:
            memo[x]=solve(x-1)+solve(x-2)+solve(x-3)
            return memo[x]
        elif x==0:
            memo[x]=1
            return 1
        else:
            return 0
    else:
        return memo[x]

def main():
    while True:
        inp=int(input())
        if inp==0:
            break
        print((solve(inp)-1)//3650+1)

main()