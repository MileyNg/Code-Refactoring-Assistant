# -*- coding: utf-8 -*-
import sys
from fractions import gcd

"""
問題文の式から、オイラーの定理
	a^{\phi(n)} = 1 mod n

よって、\phi(n) の最小公倍数を求めればよい
"""

def lcm(a, b):
    return a * b / gcd(a, b)

def interval(ax, mx):
	p = 1
	cnt = 0
	while True:
		p = (p * ax) % mx
		cnt += 1
		if p == 1:
			return cnt

for line in sys.stdin:
	dset = map(int, line.split())
	if not any(dset):
		break
	a1, m1, a2, m2, a3, m3 = dset
	e = [interval(a1, m1), interval(a2, m2), interval(a3, m3)]
	# 3つの循環の最小公倍数を求める
	e.sort(reverse=True)
	print reduce(lcm, e)