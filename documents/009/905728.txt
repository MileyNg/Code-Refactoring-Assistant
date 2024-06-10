def mlist(n, *args, **keys):
    if len(args) == 0:
        return [keys.get('default')] * n
    else:
        return [mlist(*args, **keys) for i in range(n)]


def f(n, sm):
            if n == 0:
                return int(sm == 0)
            if memo[n][sm] is not None:
                return memo[n][sm]
            memo[n][sm] = 0
            for i in range(min(10, sm + 1)):
                memo[n][sm] += f(n - 1, sm - i)
            return memo[n][sm]

try:
    memo = mlist(5, 51)
    while True:
        print f(4, int(raw_input()))
except EOFError:
    pass