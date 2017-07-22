#!/usr/bin/env python

import sys

for line in sys.stdin:

	data = line.strip()

	m = data.split("::")

	if (len(m)==3):   			# movies.dat file
		print('%s^%s^%s' % (m[0],m[1],0))
			
	elif (len(m) > 3):			# rating.dat file
		print('%s^%s^%s' % (m[1],m[2],1))				
			
