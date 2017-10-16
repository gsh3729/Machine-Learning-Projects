import math
import re
import os, sys

#read and extract words from each document
#and count the frequency of each word
def readData(pathname, words, counts):
	f = open(pathname, 'r')
	lines = f.readlines()

	for line in lines:
		if not ":" in line:
			if line.strip():
				text = re.findall(r"[\w']+", line.lower())
				for each in text:
					if len(each) > 3 and not '_' in each:
						words.append(each)
						if each in counts:
							counts[each] += 1
						else:
							counts[each] = 1
#train multinomialNB
def trainMNB(class_array, counts, training_path):
	N = 0
	Nc = {}
	prior = {}
	condprob = {}
	#get N and Nc
	for eachclass in class_array:
		dirs_temp = os.listdir( training_path+eachclass )
		docnum_inclass = len(dirs_temp)
		Nc[eachclass] = docnum_inclass
		N = N + docnum_inclass

	for eachclass in class_array:
		words_class = []
		counts_class = {}
		prior[eachclass] = float(Nc[eachclass]) / float(N)
		classp = training_path+eachclass
		doc_dirs = os.listdir( classp )
		for doc in doc_dirs:
			pn = classp + "/" + doc
			readData(pn, words_class, counts_class)
		#calculate conditional probability
		cp = {}
		for term in counts:
			if not term in counts_class:
				upper = 1.0
			else:
				upper = float(counts_class[term]+1.0)
			lower = float((len(words_class) + len(counts)))
			cp[term] = upper / lower
		condprob[eachclass]=cp
	return prior, condprob

	#apply multinomialNB
def applyMNB(testing_path, counts, p, cdp,fullpath):
	dirs_class_test = os.listdir( testing_path )
	score = {}
	words_test = []
	counts_test = {}
	w = []
	readData(fullpath, words_test, counts_test)
	for each_t in words_test:
		if each_t in counts:
			w.append(each_t)

	for cname in dirs_class_test:
		if cname != ".DS_Store":
			tmp = float(math.log(p[cname]))
			for each_ttt in w:
				tmp = tmp + float(math.log(cdp[cname][each_ttt]))
			score[cname] = tmp
	max_class = ""
	max_s = max(score.values())
	for each_s in score:
		if score[each_s] == max_s:
			max_class = each_s
	return max_class

#main
if __name__ == '__main__':
	training_path = raw_input("Enter location of training root folder: ")
	testing_path = raw_input("Enter location of test root folder: ")
	#training_path = "try/train/"
	#testing_path = "try/test/"
	words = []
	counts = {} 

	dirs_class = os.listdir( training_path )
	class_array = [];

	for classname in dirs_class:
		if classname != ".DS_Store":
			class_array.append(classname)
			classpath = training_path+classname
			dirs_doc = os.listdir( classpath )
			for doc in dirs_doc:
				pathname = classpath + "/" + doc
				readData(pathname, words, counts)
	#train MNB
	p, cdp = trainMNB(class_array, counts, training_path)

	#apply MNB for all
	print "CLASS NAME: ACCURACY"
	dirs_class_test_all = os.listdir( testing_path )
	for clname in dirs_class_test_all:
		if clname != ".DS_Store":
			ccpath = testing_path+clname
			dirs_doc_test_each = os.listdir( ccpath )
			total_sum = len(dirs_doc_test_each)
			correct = 0.0
			for e_doc in dirs_doc_test_each:
				fullpath = ccpath + "/" + e_doc
				max_ofclass = applyMNB(testing_path, counts, p, cdp,fullpath)
				if clname == max_ofclass:
					correct = correct + 1.0
			accuracy = float(correct) / float(total_sum)
			print clname + ": " + str(accuracy)
