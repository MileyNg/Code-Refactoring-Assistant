#!/usr/bin/python
# -*- coding: utf-8 -*-

n=int(raw_input())
if n:
    l=[int(x) for x in raw_input().split()]
    print min(l),max(l),sum(l)
else:
    print "0 0 0"