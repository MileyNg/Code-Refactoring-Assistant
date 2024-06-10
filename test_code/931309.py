# -*- coding: utf-8 -*-

import sys
import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    else:
        return True

def func():
    '''

    '''
    while True:
        l = map(int, raw_input().split())
        a = l[0]
        d = l[1]
        n = l[2]
        if a == 0 and d == 0 and n == 0:
            break
        elem = a
        count = 0
            
        while True:
            if is_prime(elem):
                count += 1
                if count == n:
                    print elem
                    break
            elem += d


if __name__ == '__main__':
    func()
    