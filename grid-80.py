#  File: Grid.py

#  Description: Finds the largest product of 4 numbers in the grid 

#  Student Name: Raza Retiwala

#  Student UT EID: mrr2975

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/12

#  Date Last Modified: 11/14

def main():

	in_file = open("grid.txt", "r")

	dim = in_file.readline()
	dim = dim.strip()
	dim = int(dim)

	grid = []
	sums = []

	#makes the grid
	for i in range(dim):
		line = in_file.readline()
		line = line.strip()
		row = line.split()
		for j in range(dim):
			row[j] = int(row[j])
		grid.append(row)

	#This reads every row and finds the sums of pairs of 4
	for line in grid:
		for i in range(dim-3):
			numers = []
			prod = 1
			for j in range(i, i + 4):
				numers.append(line[j])
				prod *= line[j]
				sums.append(prod)
	
	#This reads the columns...
	for j in range(dim):
		for i in range(dim -3):
			numers = []
			prod = 1 
			for k in range( i, i + 4):
				numers. append(grid[k][j])
				prod *= grid[k][j]
				sums.append(prod)

	#this reads major r --> l
	for i in range(dim-3):
		numers = []
		prod = 1
		for k in range(i, i + 4):
			numers.append(grid[k][k])
			prod = prod*grid[k][k]
			sums.append(prod)

	#this reads major l --> r
	for i in range(dim-3):
		numers = []
		prod = 1
		for i in range(i, i + 4):
			numers.append(grid[i][dim-1-i])
			prod = prod*grid[i][dim-1-i]
			sums.append(prod)



	#Every right to left diagonal 
	for j in range(dim - 3):
		for i in range(dim - 3):
			numers = []
			prod = 1
			for k in range(4):
				numers.append(grid[j+k][i+k])
				prod = prod*(grid[j+k][i+k])
				sums.append(grid[j+k][i+k])


	#every left to right diagonal
	for j in range(3, dim):
		for i in range(0, dim -3):
			sum = j + i
			numers = []
			prod = 1
			for k in range(4):
				numers.append(grid[i+k][sum-(i+k)])
				prod = prod*(grid[i+k][sum-(i+k)])
				sums.append(prod)


	print ("The greatest product is", max(sums))

main()
