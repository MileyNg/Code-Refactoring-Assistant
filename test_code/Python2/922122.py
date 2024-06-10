s=" "
x=raw_input().replace(",",s).replace(".",s).split()
print s.join([w for w in x if 2<len(w)<7])