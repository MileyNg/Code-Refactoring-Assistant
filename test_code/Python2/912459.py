from datetime import datetime

def measure(f):
    measure_start = datetime.now()
    v = f()
    print(datetime.now() - measure_start)
    return v

input = raw_input
range = xrange
    
def init():
    table = [True] * 1000001
    table[0] = False
    table[1] = False
    n = len(table)

    def prime(p):
        for i in range(p + p, n, p):
            table[i] = False
    prime(2)
    prime(3)
    prime(5)
    prime(7)
    prime(11)
    prime(13)
    
    for i in range(2, n):
        if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and
            i % 7 != 0 and i % 11 != 0 and i % 13 != 0):
            for j in range(i + i, n, i):
                table[j] = False
    return table
    
def solve(price, ps, is_prime):
    dp = [0] * ((price >> 5) + 1)

    for i in range(0, price + 1,ps[0]):
        dp[i >> 5] |= 1 << (i & 31)
    dp[0] = 1
    
    for i in range(1, len(ps)):
        cur_p = ps[i]
        r = cur_p & 31
        rest = 0
        if cur_p >= 32:
            for p in range(cur_p, price + 1, 32):
                i1 = (p - cur_p) >> 5
                i2 = p >> 5
                v = dp[i1]
                dp[i2] |= (v << r) | rest
                rest = (v >> (32 - r)) & ((1 << r) - 1)
        else:
            for p in range(cur_p, price + 1):
                dp[p >> 5] |= (dp[(p - cur_p) >> 5] >> ((p - cur_p) & 31) & 1) << (p & 31)
            
    p = -1
    for i in range(0, price + 1):
        if is_prime[i] and (dp[i >> 5] >> (i & 31)) & 1 == 1:
            p = i
    if p == -1:
        print("NA")
    else:
        print(p)
    
def main():
    table = init()
    while True:
        n, price = map(int,input().split())
        if n == 0 and price == 0:
            return
        ps = []
        for i in range(n):
            ps.append(int(input()))
        solve(price, ps, table)

main()