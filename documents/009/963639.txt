import re

ret = 0
while 1:
    try:
        line = raw_input()
    except EOFError:
        break
    num_match = re.findall('\d+', line)
    ret += sum(map(int, num_match))
print ret