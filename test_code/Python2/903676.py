def gcd(a,b):
    c = a % b
    if c == 0:
        return b
    else:
        return gcd(b, c)
    
if __name__ == "__main__":
    import sys
    a, b = [ int(e) for e in sys.stdin.readline().strip().split() ]
    print gcd(max(a,b), min(a,b))