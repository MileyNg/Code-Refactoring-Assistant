for i in range(int(raw_input())):
    s = raw_input()
    print int(''.join(sorted(s, reverse=True))) - int(''.join(sorted(s)))