mini = pre = float("inf")
def f(n):
    global mini, pre
    mini = min(mini, pre)
    pre = n
    return n - mini
print max(f(input()) for _ in xrange(input()))