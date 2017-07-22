#!/usr/bin/env python

import fileinput
import sys
import math

WordsCountForEachBook = [{'words':{}},{'words':{}},{'words':{}},{'words':{}},{'words':{}}]  # Stores the words that occur in each book

IDF_words = dict()		# Stores all the unique words that occur in all the 

WordsInEachFile = [0,0,0,0,0]	# Keep track of the number of words in each file, Each index represents the file word count
	
def Compute():
	
	global WordsCountForEachBook
	global WordsInEachFile
	global IDF_words
	
	for line in sys.stdin:	# Read from standard input stream
	
		obj = line.strip().split('\t')		# Strip the line of whitespaces and then split by tab spacing
		
		if len(obj) < 2:					# If the value contains less than 2 value, then ignore this value
			continue
		
		word = obj[0]		# Extract the word from the wrapper object
		file_id = obj[1]	# Extract the file id from which the word came and store it
		
		try:
			file_id = int(file_id)		# Convert the file_id in integer
		except ValueError:
			pass
			
		WordsInEachFile[file_id-1] += 1    # Increment the value of the the respective file_id word count by 1
		
		if word in IDF_words:			   			# This keeps track which word appears in which document and maintains a list of file ids in which it occurs
			if file_id-1 not in IDF_words[word]:	# If this word also appears in another document, 
				IDF_words[word].append(file_id-1)	# Then store its file id
		else:
			IDF_words[word] = [file_id-1] 		 	# If appearing for the first time then just store it
		
		if word in WordsCountForEachBook[file_id-1]['words']:		# If the word is already in dictionary, 
			WordsCountForEachBook[file_id-1]['words'][word] += 1	# Increase its count by 1
		
		else:
			WordsCountForEachBook[file_id-1]['words'].update({word : 1})	# If appearing for the first time then just update the dictionary
	
	TF_IDF()		# This function calculates the TF-IDF scores for each word in a document
		
def TF_IDF():		
	
	global WordsCountForEachBook
	global WordsInEachFile
	global IDF_words
	
	num_of_docs = 5.0		# Total number of documents
	
	for i in range(len(WordsCountForEachBook)):		# Since there are 5 documents so it will run from 0 till 4
		
		print("\n\n\n\t\t\t\tFor Book # " + str(i+1)+"\n\n\n")
		print("Word\t\t\tTF-score\t\t\t\tIDF-score\t\t\t\tTF*IDF-score\n\n")
		
		for key, value in WordsCountForEachBook[i]['words'].items():		# Loop through each word of a particular document
			
			tf_freqByDoc = float(value) / float(WordsInEachFile[i])		# Calculate TF
			idf_freqByDoc = math.log10(float(num_of_docs / float(len(IDF_words[key])) ))	# Calculate IDF
			
			ans = tf_freqByDoc * idf_freqByDoc	# Compute TF*IDF
			
			print(key+"\t\t\t"+str(tf_freqByDoc)+"\t\t\t"+str(idf_freqByDoc)+"\t\t\t"+str(ans))		# Show the results
		
		
			
if __name__=="__main__":
	Compute()
	
	
	
	
	
	
	
	
	
	
	
