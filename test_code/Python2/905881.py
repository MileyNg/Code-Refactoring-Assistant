from itertools import *

try:
    while True:
        a, p = 'apple', 'peach'
        b = raw_input()
        for i in count(0):
            if i >= len(b): break
            if b[i:i + len(a)] == a:
                b = b[:i] + p + b[i + len(a):]
            elif b[i:i + len(p)] == p:
                b = b[:i] + a + b[i + len(p):]
        print b
except EOFError:
    pass