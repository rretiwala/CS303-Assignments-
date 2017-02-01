#  File: CreditCard.py

#  Description: Finds type and validity of credit card 

#  Student Name: Raza Retiwala

#  Student UT EID: mrr2975

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/17

#  Date Last Modified: 11/17

def is_valid(cc_num):
	
	cc_num = str(cc_num)
	new_numbers = []

	if len(cc_num) == 15:
		for i in range(0, len(cc_num)):
			if i % 2 != 0:
				new = int(cc_num[i])*2
				if new > 9:
					new = new - 9
				new_numbers.append(new)
			else:
				new_numbers.append(int(cc_num[i]))
	elif len(cc_num) == 16:
		for i in range(0, len(cc_num)):
			if i % 2 == 0:
				new = (int(cc_num[i]))*2
				if new > 9:
					new = new - 9
				new_numbers.append(new)
			else:
				new_numbers.append(int(cc_num[i]))

	if sum(new_numbers) % 10 == 0:
		return True
	else:
		return False


def cc_type(cc_num):

	#converts to string to check the first couple characters for credit card type
	cc_num = str(cc_num)
	
	# be careful with the spacing here, add a space before the credit card name and then use the format I had in line 63
	if cc_num[0:2] == ('34') or cc_num[0:2] == ('37'):
		return (" American Express")
	elif cc_num[0:2] == ('65') or cc_num[0:3] == ('644') or cc_num[0:4] == ('6011'):
		return (' Discover')
	elif int(cc_num[0:2]) <= 55 and int(cc_num[0:2]) >= 50:
		return (' mastercard')
	elif cc_num[0] == ('4'):
		return (" Visa")
	else:
		#if not known, return blank string
		return ('')
	
def main():
	error = "Not a 15 or 16-digit number"

	cc_num = int(input("Enter 15 or 16-digit credit card number: "))

	#checks the length of the cc
	lenth = len(str(cc_num))
	if lenth > 14 and lenth < 17:
		if is_valid(cc_num):
			print ("Valid"+ cc_type(cc_num), "credit card number")
		else:
			print ("Invalid credit card number")
	else:
		print (error)

main()

