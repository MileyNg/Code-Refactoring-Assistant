#!/usr/bin/env python
# -*- coding:utf-8 -*-
#from __future__ import print_function
import time
import sys
import io
import re
import math
start = time.clock()
while 1:
    try:
        a=map(int, raw_input().split())
        b=map(int, raw_input().split())
        j=k=0
        for i in range(4):
            if b[i]==a[i]:
                j+=1
            elif b[i] in a:
                k+=1
        print j,k
    except:
        break