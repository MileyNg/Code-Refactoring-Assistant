#!/usr/bin/env python
# -*- coding:utf-8 -*-
#from __future__ import print_function
import time
import sys
import io
import re
import math
start = time.clock()

def prime(n):
    l=[True for _ in range(n+1)]
    i=2
    while i**2<=n:
        if l[i]:
            j=i+i
            while j<=n:
                l[j]=False
                j+=i
        i+=1
    return l
#    lis=[i for i in range(n+1) if l[i] and i>=2]

for n in sys.stdin:
    print (prime(int(n))).count(True)-2