p=raw_input()
print "INVALID" if len(p)<6 or p.isalpha() or p.isdigit() or p.islower() or p.isupper() else "VALID"