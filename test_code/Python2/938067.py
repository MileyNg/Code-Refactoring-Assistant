n=input()
l=[input() for _ in range(n)]
chk,ans=l[0],-1000000000
for i in range(1,n):
    chk=min(chk,l[i-1])
    if l[i]-chk>ans:
        ans=l[i]-chk
print ans