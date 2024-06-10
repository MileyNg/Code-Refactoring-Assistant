memo = [[None for i in range(51)] for j in range(5)]
memo[0][0] = 1
for i in range(1, 51):
    memo[0][i] = 0


def f(n, sm):
    if memo[n][sm] is not None:
        return memo[n][sm]
    memo[n][sm] = 0
    for i in range(min(10, sm + 1)):
        memo[n][sm] += f(n - 1, sm - i)
    return memo[n][sm]

try:
    while True:
        print f(4, int(raw_input()))
except:
    pass