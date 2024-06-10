s=raw_input()
s=s.replace(","," ")
s=s.replace("."," ")
for w in s.split():
  if 3<=len(w)<=6:print w,
print