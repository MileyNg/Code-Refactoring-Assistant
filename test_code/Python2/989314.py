def aaa(aa):
    return aa.replace('apple', 'peach')
def bbb(bb):
    return bb.replace('peach', 'apple')


a=raw_input().split()
b = 0
for i in a:
    if 'apple' in i:
        i=aaa(i)
        a[b] = i
        b+=1
        continue

    if 'peach' in i:
        i = bbb(i)
        a[b] = i
        b+=1
        continue
    b+=1

print " ".join(a)