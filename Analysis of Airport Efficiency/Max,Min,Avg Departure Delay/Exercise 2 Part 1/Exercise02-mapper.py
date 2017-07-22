#!/usr/bin/env python

import sys

for line in sys.stdin:

	data = line.strip()

	m = data.split(",")
	
	if len(m) > 7: 
		if (m[6]):
			print '%s\t%s' % (m[3], m[6])
