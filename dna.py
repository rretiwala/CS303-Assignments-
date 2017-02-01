#  File: DNA.py

#  Description: Matches DNA

#  Student Name: Raza Retiwala

#  Student UT EID: mrr2975

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 10/26

#  Date Last Modified: 10/26

def main():
	# open file for reading
	in_file = open ("./dna.txt", "r")

	# read the number of pairs
	num_pairs = in_file.readline()
	num_pairs = num_pairs.strip()
	num_pairs = int (num_pairs)

	print ("Longest Common Sequences")
	print()

	# read each pair of dna strands
	for i in range (num_pairs):
		print("Pair", str(i + 1) + ":", end="")
		st1 = in_file.readline()
		st2 = in_file.readline()

		st1 = st1.strip()
		st2 = st2.strip()

		st1 = st1.upper()
		st2 = st2.upper()

	# order strands by size
		if (len(st1) > len(st2)):
			dna1 = st1
			dna2 = st2
		else:
			dna1 = st2
			dna2 = st1

	# get all substrings of dna2

		#counts length of word
		count_len = 0

		#creates window to check
		wnd = len (dna2)

		#For no commonalities 
		flag = True

		#collects all substrands
		total = []

		while (wnd > 1):
			start_idx = 0
			while ((start_idx + wnd) <= len (dna2)):

				#creates the substrands
				sub_strand = dna2[start_idx: start_idx + wnd]
				if dna1.find(sub_strand) != -1:
					if len(sub_strand) >= count_len and ((sub_strand in total) == False):
						total.append(sub_strand)
						print ("	" + sub_strand)
						flag = False
					count_len = count_len + len(sub_strand)

				# shift window by one
				start_idx += 1
			# decrease window size
			wnd = wnd - 1

		#No common sequence 
		if flag == True:
			print ("	No Common Sequence Found")

		print()
			

	# close file
	in_file.close()

main()