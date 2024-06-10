a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
try:
    while True:
        s = raw_input()
        sm = a[s[-1]]
        for i in range(1, len(s)):
            if a[s[i - 1]] < a[s[i]]:
                sm -= a[s[i - 1]]
            else:
                sm += a[s[i - 1]]
        print sm
except EOFError:
    pass