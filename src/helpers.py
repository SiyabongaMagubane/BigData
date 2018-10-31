import numpy 
import collections
import os
import csv
import re

def toRowList(Array , row , cols):
	list = []
	for j in range(cols):
		list.append(Array[row][j])
	return list

def WriteToCSV(img_,name):
	rows,cols = img_.shape
	with open(name,"w",newline='') as my_csv:	
		csvWriter = csv.writer(my_csv)
	
		for i in range(rows):
			if isCompressRow(img_ , i ,cols):
				csvWriter.writerow([img_[i][0]])
				print("Row is compressed")
				print(i)
			else:
				list = toRowList(img_,i,cols)
				#print(list)
				csvWriter.writerow(list)
		my_csv.close()

def findsize(file_path):
	return os.path.getsize(file_path)

def WriteOriginal(name,img):
	numpy.savetxt(name,img,delimiter=",")

def isCompressRow(ArrayImage , row , cols):
	for (j) in range(cols):
		if ArrayImage[row][j] == 0:
			boolean = 1
		else:
			boolean = 0
			continue
	if boolean == 1:
		return True
	else:
		return False







