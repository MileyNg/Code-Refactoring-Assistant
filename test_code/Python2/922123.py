s=" "
x=raw_input().replace(",",s).replace(".",s).split()
x=s.join([w for w in x if 2<len(w)<7])
print x