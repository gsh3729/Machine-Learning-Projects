import math
import re
import os, sys
import random


def readData(pathname):
	f = open(pathname, 'r')
	lines = f.readlines()
	input_data = []
	for line in lines:
		if not "id" in line:
			eachline = line.split()
			floatline = []
			for each in eachline:
				floatline.append(float(each))
			floatline.append(0)
			input_data.append(floatline)
	f.close()
	return input_data

def distance(a,b):
	x = math.pow(a[1]-b[1], 2)
	y = math.pow(a[2]-b[2], 2)
	return math.sqrt(x+y)

def findK(cp, point):
	mind  = distance(cp[0], point)
	k = cp[0][0]
	for each in cp:
		if (distance(each, point) < mind):
			mind = distance(each, point)
			k = each[0]
	return k

def generateRandom(n):
	centroid=[]
	for i in range(n):
		p=[]
		p.append(i+1)
		p.append(random.uniform(0, 1))
		p.append(random.uniform(0, 1))
		centroid.append(p)
	return centroid

def SSE(centroid,data):
    sse = 0
    for i in range(len(centroid)):
        temp = 0
        for each in data:
            if each[3] == i+1:
                temp = temp + math.pow(distance(centroid[i],each),2)
        sse = sse + temp
    return sse

#main
if __name__ == '__main__':
	n = raw_input("Please enter number of clusters (k): ")
	input_path = raw_input("Please enter input file name: ")
	output_path = raw_input("Please enter output file name: ")
	n = int(n)
	#test#input_path = "test_data.txt"
	data = readData(input_path)
	#test#centroid = [[1,0,0], [2,1,1], [3,0,1], [4,1,0], [5,0.5,0.5]]
	centroid = generateRandom(n)

	changed_count = 1
	# limit your update step to a maximum of 25 iterations based on requirement
	limit = 0
	while (changed_count != 0) and (limit < 25):
		#classify each point to closest centroid point
		changed_count = 0
		for element in data:
			k = findK(centroid, element)
			if element[3] != k:
				changed_count = changed_count + 1
			element[3] = k
		#update x and y value of each center point
		for i in range(len(centroid)):
			x=0
			y=0
			t=0
			for element in data:
				if(element[3] ==i+1):
					t = t + 1
					x = x + element[1]
					y = y + element[2]
			if t!=0:
				centroid[i][1] = x/t
				centroid[i][2] = y/t
		limit = limit + 1

	#output results in a new file
	outputfile = open(output_path, 'w')
	for i in range(len(centroid)):
		outputfile.write(str(i+1) + ": ",)
		for each in data:
			if each[3] ==i+1:
				outputfile.write(str(int(each[0])) + " ",)
		outputfile.write('\n')
	outputfile.write('\n')
	outputfile.write("The value of SSE: ",)
	ssevalue = SSE(centroid, data)
	outputfile.write(str(ssevalue))
	outputfile.close()













