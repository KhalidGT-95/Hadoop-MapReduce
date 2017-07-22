#!/usr/bin/env python

import fileinput
import sys
import os

try:
	input_file = os.environ['map_input_file']	# Gets the current file URL that mapper is currently reading from
except KeyError: 
	print("Cannot get the filename !!!")
	

data_values = input_file.strip().split('/')		# Get the URL of the file
		
###### Important Step !!! #######
id_of_file = data_values[-2].split('-')[1]		# Get the id of the file by getting the directory name and splitting it so that at the end we get file id 

for line in sys.stdin:
	data = line.strip().split(' ')				# Split the line using space as a delimiter
	
	for word in data:		
		if not word.isspace():						# If the word is not a space 
			print('%s\t%s' % (word,id_of_file))		# Send the word and id of the file as a key value pair
	
	

