from itertools import product

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(s):
    for a in range(1, 26, 2):
        if a == 13: continue
        for b in range(26):
            x = ''.join(chr(ord('a') + (a * i + b) % 26) for i in range(26))
            t = s.translate(str.maketrans(x, alphabet))
            if 'this' in t or 'that' in t:
                return t

n = int(input())
for i in range(n):
    s = input()
    print(decrypt(s))