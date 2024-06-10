def isPalindrome(n):
    s = str(n); l = len(s);
    for i in xrange(l/2):
        if s[i]!=s[-1-i]:
            return False
    return True
n = input()
p = q = n
while isPalindrome(p)==False:
    p += 1
while isPalindrome(q)==False:
    q -= 1
print q if abs(n-q)<=abs(p-n) else p