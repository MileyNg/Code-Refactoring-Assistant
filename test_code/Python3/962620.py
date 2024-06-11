s = input()
print(''.join(c.lower() if c.isupper() else c.upper() if c.islower() else c for c in s))