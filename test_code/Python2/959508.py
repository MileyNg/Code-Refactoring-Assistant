# -*- coding: utf-8 -*-

def dfs(num, dem, k, cur_num, prd, p, q, a, n):

    #print num, dem, k, cur_num, prd
    #time.sleep(0.5)
    if num == 0:
        #print "result: " + str(result)
        return 1

    result = 0

    i = cur_num
    while prd * i <= a:
        #print i, num, dem, k, cur_num, prd
        if (n - k) * dem < num * i:
            break
        if num * i < dem:
            i += 1
            continue

        result += dfs((num * i) - dem, dem * i, k + 1, i, prd * i, p, q, a, n)
        i += 1

    return result

def func():
    while True:

        p, q, a, n = map(int, raw_input().split())

        if p == 0 and q == 0 and a == 0 and n == 0:
            break

        print dfs(p, q, 0, 1, 1, p, q, a, n)
        
    return None

if __name__ == '__main__':
    func()
    