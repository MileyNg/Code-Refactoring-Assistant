def gcd(u, v):
    if (v == 0): return u
    return gcd(v, u % v)

def lcm(u, v):
    return (u * v) // gcd(u, v)

while 1:
    try:
        inp = input()
    except EOFError:
        break
    else:
        u, v = inp.split(' ')
        u = int(u)
        v = int(v)
        print(gcd(u, v), lcm(u, v))