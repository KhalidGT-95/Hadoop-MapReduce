#!/usr/bin/env python

from operator import itemgetter
import sys

movieIdAndRating = dict()
movieAndTitle = dict()

max_avg_rating = dict()

def ratingFunction(idOfMovie,rating):
	global movieIdAndRating
	
	if idOfMovie in movieIdAndRating:
		movieIdAndRating[idOfMovie]['rating'] += rating
		movieIdAndRating[idOfMovie]['occurences'] += 1
		movieIdAndRating[idOfMovie]['runningavg'] = float(movieIdAndRating[idOfMovie]['rating'] / movieIdAndRating[idOfMovie]['occurences'])
		max_avg_rating[idOfMovie] = movieIdAndRating[idOfMovie]['runningavg']
		
	else:
		movieIdAndRating[idOfMovie] = {'rating' : rating , 'occurences' : 1 , 'runningavg' : rating}
		max_avg_rating[idOfMovie] = float(rating)
	

def Engine():

	flag = 0
	global movieIdAndRating
	max_avg_rating = None
	
	Best_Movie_By_Rating = None
	
	for line in sys.stdin:

		temp = line.strip().split('^')
		
		if int(temp[2]) == 0:			# This one has movie movie id and title
			#print('here')
			if flag == 0:
				max_avg_rating = max(movieIdAndRating.iteritems() , key = itemgetter(1))			
				flag = 1
				
				if (temp[0]) == (max_avg_rating[0]):
					#print('here')
					Best_Movie_By_Rating = temp[1]
				
			else:					
				if float(temp[0]) == float(max_avg_rating[0]):
					Best_Movie_By_Rating = temp[1]
					
		elif int(temp[2]) == 1:				# This one has movie id and rating
			#print('here')
			ratingFunction(temp[0],float(temp[1]))
			
		#print(temp)
	print("\n")	
	print(Best_Movie_By_Rating + " has the maximum average rating\n")	


Engine()
