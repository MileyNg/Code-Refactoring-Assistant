def is_palindrome(string):
    for i in xrange(len(string) / 2):
        if string[i] != string[-1 - i]:
            return False
    return True


ret = 0
while 1:
    try:
        if is_palindrome(raw_input()):
            ret += 1
    except EOFError:
        break
print ret