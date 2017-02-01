# File: Goldbach.py
# Description: Provides evidence for goldbach's conjecture
# Student Name: Raza Retiwala
# Student UT EID: mrr2975
# Course Name: CS 303E
# Unique Number: 51200
# Date Created: 10/10/16
# Date Last Modified: 10/10/16

def is_prime(num):
	num_orig = num
	divisor = 2
	limit = int(num**.5) + 1
	is_prime = True
	while (divisor < limit) and is_prime:
		if (num % divisor == 0):
			is_prime = False
		divisor += 1
	if (is_prime) and (num!=1) and (num !=0):
		return is_prime
	else:
		return False 

def main():   
	low = int(input("Enter a lower limit:"))
	up = int(input("Enter an upper limit:"))
	
	while (low < 4) or (low % 2 != 0) or (up % 2 != 0) or (up < low):
		low = int(input("Enter a lower limit:"))
		up = int(input("Enter an upper limit:"))
	
	for i in range(low, up + 1, 2):
		sum_of_prime = str(i)
		for j in range(2,int(i/2)+1):
			if is_prime(j):
				remainder = i - j
				if is_prime(remainder):
					sum_of_prime = sum_of_prime + " = " + str(j) + " + " + str(remainder)
		print(sum_of_prime)

main()