uni = {}
common = ['être', 'avoir', 'aller', 'faire']

def er_verbs(a):

	#deals with pronominal verbs 
	'''
	if a[:3] == "se ":
		a = a[3::]
	'''

	stem = a[:-2]

	if a[-4] == "é":
		stem = stem[-1]
		
	je = stem + 'e'
	tu = stem + 'es'
	il = stem + 'e'

	# boot verbs 
	if a[-3:] == "ger":
		nous = stem + 'eons'

	#another type boot verbs
	elif a[-3:] == 'cer':
		nous = stem[:-1] + 'çons'
	else:
		nous = stem + 'ons'
	vous = stem + 'ez'
	ils = stem + 'ent'

	conjugations = [je, tu, il, nous, vous, ils]
	uni[a] = conjugations
	print(a)
	print(je + "	" + nous)
	print(tu + "	" + vous)
	print(il + "	" + ils)


def ir_verbs(a):
	stem = a[:-2]

	je = stem + 'is'
	tu = stem + 'is'
	il = stem + 'it'
	nous = stem + 'issons'
	vous = stem + 'issez'
	ils = stem + 'issent'

	conjugations = [je, tu, il, nous, vous, ils]
	uni[a] = conjugations
	print(a)
	print(je + "	" + nous)
	print(tu + "	" + vous)
	print(il + "	" + ils)


def re_verbs(a):
	stem = a[:-2]

	je = stem + 's'
	tu = stem + 's'
	il = stem + ''
	nous = stem + 'ons'
	vous = stem + 'ez'
	ils = stem + 'ent'

	conjugations = [je, tu, il, nous, vous, ils]
	uni[a] = conjugations
	print(a)
	print(je + "	" + nous)
	print(tu + "	" + vous)
	print(il + "	" + ils)


def main():
	verb = input("Enter a verb:")

	in_file = open("1.txt", "r")

	for line in in_file:
		line = line.strip()
		line = line.split()
		uni[line[0]] = line[1:]

	in_file.close()

	# checks if the conjugation is in the dictionary already
	if verb in uni:

		#sets each conjugation
		je = uni[verb][0]
		tu = uni[verb][1]
		il = uni[verb][2]
		nous = uni[verb][3]
		vous = uni[verb][4]
		ils = uni[verb][5]

		#prints out results
		print(verb)
		print(je + "	" + nous)
		print(tu + "	" + vous)
		print(il + "	" + ils)

	#checks if verb is one of the irregulars
	elif verb in common:
		new = input("Do you know the conjugations? Yes or No: ")
		if new == "Yes":
			conjug = input("Give me the conjugations without the pronouns: ")
			conjug = conjug.split()
			uni[verb] = conjug
		else:
			print("Sorry! We don't know.")

		dictionary = open("1.txt", "w")
		for item in uni:
			dictionary.write(item + " ")
			for k in uni[item]:
				dictionary.write(k + " ")
			dictionary.write("\n")
	#conjugates the verb otherwise
	else:
		if verb[-2:] == "er":
			er_verbs(verb)
		elif verb[-2:] == "ir":
			ir_verbs(verb)
		elif verb[-2:] == "re":
			re_verbs(verb)

		#if verb doesn't fit any of the last couple criteria, then ask the user if 
		else:
			new = input("Do you know the conjugations? Yes or No: ")
			if new == "Yes":
				conjug = input("Give me the conjugation without the pronouns: ")
				conjug = conjug.split()
				uni[verb] = conjug
			else:
				print("Sorry! We don't know.")

		dictionary = open("1.txt", "w")
		for item in uni:
			dictionary.write(item + " ")
			for k in uni[item]:
				dictionary.write(k + " ")
			dictionary.write("\n")
	''''
	for item in uni:
		print (item, uni[item])
	'''

	in_file.close()


main()