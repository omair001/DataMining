"""
"
" This script gets all the unique words from the output file and outputs it in a single row
" Written by Omair
"
"""
import csv
import re
import string
from collections import defaultdict
import math

""" open file """
file = open('train_stem1.csv')
reader = csv.reader(file)
data = list(reader)
words = []
frequency={}
IDF = {}
countVector = {}
outputFile = open('output1.csv', 'a')
outputWriter = csv.writer(outputFile)

""" obtain a list of unique words in all the reviews """
for row in data:
	ri = row[0].split()
	for word in ri:
		if word not in words:
			words.append(word)	
		if word not in frequency:
			frequency.update({word:1})
		else:
			frequency.update({word:frequency.get(word) + 1})

""" Remove rare words """			
for word in frequency:
	if frequency.get(word) < 3:
		words.remove(word)

wordcount = [[]]
wordcount[0] =words

""" the counting matrix is going to count the occurrences of unique words in this row used for calculations later """			
for row in data[1:]:
	ri = row[0].split()
	w =[0] * len(words)
	for word in ri:
		if word in words:
			w[words.index(word)] = w[words.index(word)] +1
	wordcount.append(w)

""" counts the occurence of a word in each row """	
for i in range(0,len(words)):
	wCount = 0
	for row in wordcount[1:]:
		if row[i] > 0:
			wCount +=1
	countVector.update({words[i]:wCount})

""" IDF calculation """	
for  key, value in countVector.iteritems():
	IDF.update({key: math.log10(40000/value)})

""" TF-IDF calculation """		
for row in wordcount[1:]:
	for word in words:
		row[words.index(word)] = row[words.index(word)] * float(IDF.get(word)) 
file.close()	

for row in wordcount:
	outputWriter.writerow(row)

 		
"""this is the list of words"""
#print("words: "+str(words))
"""this was a count of the number of occurrences of each word in a map so you could see how often they occur in the whole string(was using it to test)""" 
#print("wordcount: "+str(wordcount))

outputFile.close()