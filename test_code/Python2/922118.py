s=raw_input().replace(","," ").replace("."," ").split()
s=" ".join([w for w in s if 2<len(w)<7])
print s