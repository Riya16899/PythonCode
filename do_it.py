#P(Category) = (No. of documents classified into the category) divided by (Total number of documents)

from __future__ import division
import os
path1, dirs1, files1 = next(os.walk("/home/redcliff/Naive_Bayes/Auto"))
path2, dirs2, files2 = next(os.walk("/home/redcliff/Naive_Bayes/computer"))
path3, dirs3, files3 = next(os.walk("/home/redcliff/Naive_Bayes/sports"))
f1 = open('/home/redcliff/Naive_Bayes/Auto/Doc1','r')
f2 = open('/home/redcliff/Naive_Bayes/Auto/Doc2','r')
f3 = open('/home/redcliff/Naive_Bayes/another/Merge','w')

# step 1:
def total_file_count(files1,files2,files3):
	file_count1 = len(files1)
	file_count2 = len(files2)
	file_count3 = len(files3)
	total_files = file_count1+file_count2+file_count3

	print(file_count1 / total_files)
	print(file_count2 / total_files)
	print(file_count3 / total_files)

while True:
	if (os.stat('/home/redcliff/Naive_Bayes/computer/Doc2').st_size==0) == True:
		print("Doc2 is empty")
		break
	elif (os.stat('/home/redcliff/Naive_Bayes/computer/Doc1').st_size==0) == True:
		print("Doc1 is empty")
	



def occurance_allDoc():
		f4 = open('/home/redcliff/Naive_Bayes/another/Merge','r')
		content4 = f4.read().split() #len(content4) .. All the words in every document from AUTO
		print("total word %s " % (len(content4)))
		total_wordcount = {}

		for word in content4:
			if word not in total_wordcount:
				total_wordcount[word] = 1
			else :
				total_wordcount[word] += 1
		print("unique word lengh %s " % (len(total_wordcount))) #unique word from all Doc in Auto
		for k4,v4 in total_wordcount.items():
			if k4 == 'Saturn':
				print("occurnce of 'Saturn' is %d " % (v4+1)) # +1 here mensioned

#occurance_allDoc()



class single_file_count:
	def __init__(self,file_address,find_word):
		self.file_address = file_address
		self.find_word = find_word

	def display(self):
		file_name = open(self.file_address,'r')
		content = file_name.read().split()
		wordcount = {}
		for word in content:
			if word not in wordcount:
				wordcount[word] = 1
			else:
				wordcount[word] += 1
		for key,value in wordcount.items():
			if key == self.find_word:
				print(key,value+1)
		
				

b = single_file_count('/home/redcliff/Naive_Bayes/another/Merge','Saturn')
c = b.display()




print("...............................................")
variable_one = "Apple"
variable_two = "Orange"
print "I would like an %s, not an %r" % (variable_one, variable_two)








