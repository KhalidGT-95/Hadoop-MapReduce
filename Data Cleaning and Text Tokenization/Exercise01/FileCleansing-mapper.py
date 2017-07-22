#!/usr/bin/env python

from __future__ import print_function	# Since i am working in python2.7 so need it

import sys

for line in sys.stdin:		# Read line by line using stdin
	data = line.strip()		# Strip the of spaces
	if data != '':			# If the line is not blank
		print(data)			# Then output the line
		

