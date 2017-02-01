#  File: Spiral.py

#  Description: Finds the 8 numbers around a number in a spiral

#  Student Name: Raza Retiwala

#  Student UT EID: mrr2975

#  Partner Name: Roshini Saravanakumar 

#  Partner UT EID: Rs48876

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/20

#  Date Last Modified: 11/21

def create_grid(dim):
	dim_orig = int(dim)

	grid = []
	for i in range(0, dim):
		grid.append([])

	for i in range(dim):
		for k in range(dim):
			grid[i].append(0)


	top = 0
	left = 0
	bottom = dim - 1
	right = dim - 1
	number = dim**2 

	while dim > 0:

		#TOP
		count = right
		while count >=left:
			grid[top][count] = number
			count -=1
			number -= 1

		
		#LEFT
		count = top+1
		while count <=bottom:
			grid[count][left] = number
			count +=1
			number -=1

		#Bottom
		count = left + 1
		while count < right:
			grid[bottom][count] = number
			count +=1
			number -=1


		#Right
		count = bottom
		while count > top:
			grid[count][right] = number
			count -=1
			number -=1

		top +=1
		left +=1
		right -=1
		bottom -=1
		dim -=2
		

		grid[dim_orig // 2][dim_orig // 2] = 1

	return grid

def main():
	dim = int(input('Enter dimension: '))
	goal = int(input('Enter number in spiral: '))

	if dim % 2 == 0:
		dim +=1 

	if (goal > dim**2) or (goal < 1):
		print ('Number not in range')
	else:
		grid = create_grid(dim)
		
		for item in grid:
			first = grid.index(item)
			if goal in item:
				second = item.index(goal)
				break

		flag = False
		if (first == 0) or (first == dim-1) or (second == 0) or (second == dim-1):
			print ("Number on Outer Edge")
		else:
			flag = True

		if flag:
			print (grid[first -1][second -1], grid[first -1][second], grid[first -1][second +1])
			print (grid[first][second -1], grid[first][second], grid[first][second + 1])
			print (grid[first+ 1][second -1], grid[first+ 1][second], grid[first+ 1][second + 1])



main()

