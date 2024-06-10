#!/usr/bin/env python

tmp_max = [0,0,0]

import sys
for line in iter(sys.stdin.readline, ""):
	if int(line) > tmp_max[2]:
		tmp_max[2] = int(line)
		if tmp_max[2] > tmp_max[1]:
			tmp_max[1],tmp_max[2] = tmp_max[2],tmp_max[1]
			if tmp_max[1] > tmp_max[0]:
				tmp_max[0],tmp_max[1] = tmp_max[1],tmp_max[0]

print tmp_max[0]
print tmp_max[1]
print tmp_max[2]