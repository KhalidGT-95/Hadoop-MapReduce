#!/usr/bin/env python

from operator import itemgetter
import sys
import operator

word = None
airports = dict()

top10_dict = dict()

def FindTop10(values):
	
	sorted_list = sorted(values.items(),key=operator.itemgetter(1))
	
	print("\nThe top 10 airports sorted by their Average arrival delay\n")
	for i in range(10):
		print("Airport : "+sorted_list[i][0] + " , Average Delay : "+ str(sorted_list[i][1]))
	
def Engine():
	
	for line in sys.stdin:
		
		line = line.strip()

		word,value = line.split('\t',1)

		try:
			value = float(value)
		
		except ValueError:
			continue

		if word in airports:
			airports[word]['totalvalue'] += value

			airports[word]['totaloccurence'] += 1

			airports[word]['runningavg'] = airports[word]['totalvalue'] / airports[word]['totaloccurence']
			
			top10_dict[word] = airports[word]['runningavg']

		else:
			airports[word] = {'max':value,'min':value,'totalvalue':value,'totaloccurence':1,'runningavg':0}
			top10_dict[word] = value

	return top10_dict

if __name__=="__main__":

	result = Engine()

	FindTop10(result)
