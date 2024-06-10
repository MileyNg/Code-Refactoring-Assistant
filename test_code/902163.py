m = []
for i in range(10):
    m.append(input())
m.sort(reverse=True)
print '\n'.join(map(str, m[:3]))