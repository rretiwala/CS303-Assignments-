#  File: Books.py

#  Description: Compares diction between two authors

#  Student Name: Raza Retiwala

#  Student UT EID: mrr2975

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 12/1	

#  Date Last Modified: 12/2

word_dict = {}
def create_word_dict():
	#creates dictionary 
	dictionary = open("words.txt", "r")

	for line in dictionary:
		line = line.strip()
		word_dict[line] = 1

	dictionary.close()

# Removes punctuation marks from a string
def parseString (st):
	end_line = ''

	for i in range(len(st)):

		if (st[i].isalpha()) or (st[i].isspace()):
			if st[i] != "s":
				end_line += st[i]
			elif st[i] == "s" and st[i-1] != "'":
				end_line += st[i]
			else:
				end_line += " "
		elif st[i] == "'" and i != len(st)-1: 
			if st[i+1] != "s":
				end_line += st[i]
			else:
				end_line += " "
		elif st[i] == "'" and i == len(st)-1:
			end_line += st[i]
		else:
			end_line += " "

	return end_line

# Returns a dictionary of words and their frequencies
def getWordFreq (file):

	#opens book
	book = open(file, "r")

	#book dictionary 
	book_dict = {}

	#list of all upper 
	all_upper = []

	#total worlds
	total = 0

	for line in book:
		#new line
		line = line.strip()

		#removes all punctuation 
		line = parseString(line)

		#creates list of words
		list_word = line.split()

		
		for word in list_word:
			#if letter begins with a capital, add to the list of capital words
			if (word[0]).isupper():
				all_upper.append(word)

			#if it's already in the dictionary, increment the freq by 1
			elif word in book_dict:
				book_dict[word] += 1

			#add to dictionary
			else:
				book_dict[word] = 1

	for item in all_upper:
		word = item.lower()
		
		#if word is in book dictionary then increment by 1
		if word in book_dict:
			book_dict[word] +=1
		elif word in word_dict:
			book_dict[word] = 1

	book.close()
	return book_dict


# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
	distinct1 = len(freq1)
	distinct2 = len(freq2)

	total1 = 0
	total2 = 0

	for key in freq1:
		total1 += freq1[key]

	for key in freq2:
		total2 += freq2[key]

	percent1 = (distinct1 / total1)*100
	percent2 = (distinct2 / total2)*100

	percent1 = format(percent1, ".10f")
	percent2 = format(percent2, ".10f")

	a1_set = set(freq1.keys())
	a2_set = set(freq2.keys())

	difference_1 = a1_set - a2_set
	difference_2 = a2_set - a1_set 

	freq_a1 = 0
	freq_a2 = 0

	NOW_a1 = len(difference_1)
	NOW_a2 = len(difference_2)

	for item in difference_1:
		freq_a1 += freq1[item]
	for item in difference_2:
		freq_a2 += freq2[item]


	relative_freq1 = (freq_a1 / total1)*100
	relative_freq2 = (freq_a2 / total2)*100

	relative_freq1 = format(relative_freq1, ".10f")
	relative_freq2 = format(relative_freq2, ".10f")

	#all of author 1 stats
	print (author1)
	print ("Total distinct words =", distinct1)
	print ("Total words (including duplicates) =", total1)
	print ("Ratio(% of total distinct words to total words) =", percent1)
	print ()

	#all of author 2 stats
	print (author2)
	print ("Total distinct words =", distinct2)
	print ("Total words (including duplicates) =", total2)
	print ("Ratio(% of total distinct words to total words) =", percent2)

	#comparisons author 1
	print ()
	print (author1, "used", NOW_a1, "that", author2, "did not use." )
	print ("Relative frequency of words used by", author1, "not in commom with", author2, "=", relative_freq1)

	#comparisons author 2
	print ()
	print (author2, "used", NOW_a2, "that", author1, "did not use." )
	print ("Relative frequency of words used by", author2, "not in commom with", author1, "=", relative_freq2)


	

def main():
	# Create word dictionary from comprehensive word list
	create_word_dict()

	# Enter names of the two books in electronic form
	book1 = input ("Enter name of first book: ")
	book2 = input ("Enter name of second book: ")
	print()

	# Enter names of the two authors
	author1 = input ("Enter last name of first author: ")
	author2 = input ("Enter last name of second author: ")
	print() 

	# Get the frequency of words used by the two authors
	wordFreq1 = getWordFreq (book1)
	wordFreq2 = getWordFreq (book2)

	# Compare the relative frequency of uncommon words used
	# by the two authors
	wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
