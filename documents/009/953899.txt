import re
snakeA = re.compile('>\'(=+)#\\1~$')
snakeB = re.compile('>\^(Q=)+~~$')
for i in xrange(input()):
    s = raw_input()
    if snakeA.match(s) is not None:
        print "A"
    elif snakeB.match(s) is not None:
        print "B"
    else:
        print "NA"