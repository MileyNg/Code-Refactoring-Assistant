import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    ret = 0
    for i in range(N):
        if isPrime(int(sys.stdin.readline().strip())):
            ret += 1
    print ret