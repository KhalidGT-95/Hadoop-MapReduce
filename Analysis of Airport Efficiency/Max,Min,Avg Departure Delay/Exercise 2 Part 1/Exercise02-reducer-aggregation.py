#!/usr/bin/env python

from operator import itemgetter
import sys

airports = dict()

def Engine():	
	
	for line in sys.stdin:

		line = line.strip()

		word,value = line.split('\t',1)
		
		try:
			value = float(value)
		
		except ValueError:
			continue
	
		if word in airports:
			if airports[word]['max'] < value:
				airports[word]['max'] = value

			if airports[word]['min'] > value:
				airports[word]['min'] = value
		
			airports[word]['totalvalue'] += value

			airports[word]['totaloccurence'] += 1

			airports[word]['runningavg'] = airports[word]['totalvalue'] / airports[word]['totaloccurence']

		else:
			airports[word] = {'max':value,'min':value,'totalvalue':value,'totaloccurence':1,'runningavg':value}
	
	print("\n\t\tAirport <Name,Max. departure delay, Min. departure delay, Avg. departure delay>\n")
	for i in airports:
		print("< "+ i +" , "+str(airports[i]['max'])+" , "+str(airports[i]['min'])+ " , "+str(airports[i]['runningavg'])+" >")	
			
	
if __name__ == "__main__":
	Engine()
