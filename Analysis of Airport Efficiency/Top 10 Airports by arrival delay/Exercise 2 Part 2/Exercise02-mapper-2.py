#!/usr/bin/env python

import sys

for line in sys.stdin:

	data = line.strip()

	m = data.split(",")
	
	if len(m) > 8: 
		if (m[8]):
			print '%s\t%s' % (m[3], m[8])
