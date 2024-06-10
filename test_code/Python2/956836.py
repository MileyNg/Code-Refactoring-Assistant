import re
print ' '.join(filter(lambda a: 3 <= len(a) <= 6, re.split('[ ,.]', raw_input())))