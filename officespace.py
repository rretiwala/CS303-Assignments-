#  File: Officespace.py

#  Description: 

#  Student Name: Raza Retiwala

#  Student UT EID: mrr2975	

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51920

#  Date Created: 1/27

#  Date Last Modified: 1/30

import math
import sys

class Point (object):
	# constructor 
	def __init__ (self, x = 0, y = 0):
		self.x = x
		self.y = y

	# get distance
	def dist (self, other):
		return math.hypot (self.x - other.x, self.y - other.y)

		# get a string representation of Point
	def __str__ (self):
		return str(self.x) + " " + str(self.y)

	# test for equality
	def __eq__ (self, other):
		tol = 1.0e-16
		return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

a = []

for line in sys.stdin:
	line = line.strip()
	a.append(line)

test_1 = a[0:5]
test_2 = a[5:9]


def make_graph(inputs):
	dimensions = inputs[0].split()

	for i in range (len(dimensions)):
		dimensions[i] = int(dimensions[i])
	
	x = dimensions[0]
	y = dimensions[1]
	
	graph = []
	
	for p in range(y+1):
		graph.append([])
	
		
	idx = 0
	for k in range(y+1):
		if idx <= (y):
			for i in range(x+1):
				graph[idx].append(Point(i, k))
		else:
			continue
		idx +=1
		
	'''
	
	for item in graph:
		print (item)
		print  ()
		
	
	'''
	return graph
	
def main(variable):
	graph = make_graph(variable)

	dimensions = variable[0].split()

	for i in range(len(dimensions)):
		dimensions[i] = int(dimensions[i])

	x = dimensions[0]
	y = dimensions[1]

	area = x*y
	print ("Total", area)
	
	number_of_employees = int(variable[1])
	employee_names = {'Contested':0}
	employee_ordered = ['Contested']
	
	for i in range(number_of_employees):
		
		# gets employee information and makes a list of strings
		employee_data = variable[i+2].split()
		
		#sets employee name
		employee_name = employee_data[0]

		if employee_name not in employee_ordered:
			employee_ordered.append(employee_name)
		else:
			continue
		
		#keeps count of how much space each employee has
		employee_names[employee_name] = 0
		
		ll_point = Point(int(employee_data[1]),int(employee_data[2]))
		lr_point = Point(int(employee_data[3]),int(employee_data[2]))
		ul_point = Point(int(employee_data[1]),int(employee_data[4]))
		ur_point = Point(int(employee_data[3]),int(employee_data[4]))
		
	
		#print (str(ll_point) +'| '+ str(lr_point) +'| ' + str(ul_point)+'| ' + str(ur_point))
		
		
		ul_split = str(ul_point).split()
		lr_split = str(lr_point).split()
		
		'''
		print (ul_split)
		print (lr_split)
		print ()
		
		'''
		begin_x = int(ul_split[0])
		stop_x = int(lr_split[0])
		
		stop_y = int(ul_split[1])
		begin_y = int(lr_split[1])
		
		#print (begin_x, stop_x, begin_y, stop_y)
		
		for i in range(begin_y, stop_y):
			for k in range(begin_x, stop_x):
				if (type(graph[i][k]) == str):
					graph[i][k] = "Contested"
				else:
					graph[i][k] = employee_name


	for i in range(len(graph)):
		for k in range(len(graph[i])):
			if type(graph[i][k]) == str:
				#print (graph[i][k], k, i)
				employee_names[graph[i][k]] += 1
			else:
				graph[i][k] = str(graph[i][k])
	

	total = 0

	for item in employee_names:
		total += employee_names[item]

	un_al = area-total
	print ("Unallocated", un_al)

	for item in employee_ordered:
		print (item, employee_names[item])

	
	print ()
	
main(test_1)
main(test_2)