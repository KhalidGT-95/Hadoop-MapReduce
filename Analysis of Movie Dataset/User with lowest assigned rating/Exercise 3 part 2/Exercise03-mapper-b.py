#!/usr/bin/env python

import sys

for line in sys.stdin:

	data = line.strip()

	m = data.split("::")
	
	print('%s^%s' % (m[0],m[2]))

