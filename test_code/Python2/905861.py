try:
    mx, mn = 0, 100000
    while True:
        p = float(raw_input())
        mx = max(mx, p)
        mn = min(mn, p)
except EOFError:
    pass
print mx - mn