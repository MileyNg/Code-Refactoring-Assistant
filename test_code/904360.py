import re
r=re.compile("UU|DD|RR|LL")
for i in range(input()):print "Yes" if r.search(raw_input()) is None else "No"
	