#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
i = 0
inn=[]
for i in sys.stdin:
    i=int(i)
    if i==0 and len(inn)>0:
        print inn[-1]
        inn.pop()
    elif i==0 and len(inn)==0:
        sys.exit()
    elif i!=0:
        inn.append(i)
for i in inn:
    print i