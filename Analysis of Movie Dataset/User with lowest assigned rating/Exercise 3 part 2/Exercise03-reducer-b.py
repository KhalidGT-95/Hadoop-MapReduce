#!/usr/bin/env python

from operator import itemgetter
import sys

movieIdAndRating = dict()
userLowest = dict()

def ratingFunction(UserId,rating):
	
	global movieIdAndRating
	global userLowest
	
	if UserId in movieIdAndRating:
		movieIdAndRating[UserId]['rating'] += rating
		movieIdAndRating[UserId]['occurences'] += 1
		movieIdAndRating[UserId]['runningavg'] = (movieIdAndRating[UserId]['rating'] / movieIdAndRating[UserId]['occurences'])
		
		if movieIdAndRating[UserId]['occurences'] >= 40:
			userLowest[UserId] = movieIdAndRating[UserId]['runningavg']
					
	else:
		movieIdAndRating[UserId] = {'rating' : rating , 'occurences' : 1 , 'runningavg' : rating}

	
def Output(data):

	final_output = min(data.iteritems() , key = itemgetter(1))
	
	print("\nThe User which assigned the minimum rating is : " + str(final_output[0]) + " , with a average rating of : " + str(final_output[1]))
	print("\n")
	
	
def Engine():

	global movieIdAndRating
	global userLowest
	
	for line in sys.stdin:

		temp = line.strip().split('^')
		
		ratingFunction(temp[0],float(temp[1]))

	Output(userLowest)

if __name__=="__main__":

	Engine()
