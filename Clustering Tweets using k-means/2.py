import math
import re
import os, sys
import random
import json

def Jac_dis(centroid,data):
	temp = 0
	for each in centroid:
		if each in data:
			temp = temp + 1
	dis = float(temp) / float((len(centroid)+len(data)-temp))
	return 1-dis

def find_centroid(data,centroid):
	for i in range(len(centroid)):
		total_distance = 10000
		key = centroid[i]
		for j in data:
			if data[j][2] == centroid[i]:
				temp = 0
				for k in data:
					if data[k][2] == centroid[i]:
						temp = temp + Jac_dis(data[j][0],data[k][0])
				if temp <= total_distance:
					total_distance = temp
					key = j
	centroid[i] = key
	return centroid

def SSE(centroid,data):
    sse = 0
    for i in range(len(centroid)):
        temp = 0
        for each in data:
            if data[each][2] == centroid[i]:
                temp = temp + math.pow(Jac_dis(data[each][0], data[centroid[i]][0]),2)
        sse = sse + temp
    return sse

#MAIN
if __name__ == '__main__':
	n = raw_input("Please enter number of clusters: ")
	seed_path = raw_input("Please enter initialSeedsFile name: ")
	json_path = raw_input("Please enter TweetsDataFile name: ")
	output_path = raw_input("Please enter output file name: ")
	f=open(json_path, 'r')
	lines = f.readlines()
	data = []
	for line in lines:
		data.append(line)
	f.close()

	ppdata = []
	for each in data:
		js = json.loads(each)
		temp = []
		temp.append(js['id'])
		temp.append(js['text'])
		ppdata.append(temp)
	ppdict = {	}
	for i in range(len(ppdata)):
		temp = []
		temp_temp = []
		eachline = ppdata[i][1].split()
		for each in eachline:
			if not 'RT' in each:
				if not '@' in each:
					if not 'http' in each:
						if not '...' in each:
							e = each.strip(':,#-.()|//')
							temp.append(e)
		temp_temp.append(temp)
		temp_temp.append(10)	
		temp_temp.append(0)				
		ppdict[ppdata[i][0]] = temp_temp

	c = open(seed_path,'r')
	lines = c.readlines()
	centroid = []
	for each in lines:
		each = each.replace(',','')
		centroid.append(int(each))
	c.close()

	change_count = 1
	while change_count != 0:
		change_count = 0
		for a in ppdict:
			temp1 = ppdict[a]
			for b in centroid:
				temp2 = ppdict[b]
				distance = Jac_dis(temp2[0],temp1[0])
				if distance <= temp1[1]:
					ppdict[a][1] = distance
					if ppdict[a][2] != b:
						change_count = change_count + 1
					ppdict[a][2] = b
		centroid = find_centroid(ppdict,centroid)
	
	#output results in a new file
	outputfile = open(output_path, 'w')
	for i in range(len(centroid)):
		outputfile.write(str(i+1) + ": ",)
		for each in ppdict:
			if ppdict[each][2] == centroid[i]:
				outputfile.write(str(each) + " ",)
		outputfile.write('\n')
	outputfile.write('\n')
	outputfile.write("The value of SSE: ",)
	ssevalue = SSE(centroid, ppdict)
	outputfile.write(str(ssevalue))
	outputfile.close()


	