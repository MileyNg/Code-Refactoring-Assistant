a,b = map(int, raw_input().split())
f = float(a)/float(b)
d = int(f)
r = a%b
print "%s %s %f"%(d, r, f)