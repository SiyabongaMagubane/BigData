import cv2
import numpy 
import collections
import os
import csv
import re

from PIL import Image
#from helper_fnc import *
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


def toArray(Image_):
	image = Image.open(Image_)
	ArrayImage = numpy.array(image)
	#print(ArrayImage.shape)
	rows,cols,channel = ArrayImage.shape

	#cv2.imshow('image_original',ArrayImage)

	img_b , img_g , img_r = cv2.split(ArrayImage)

	print(img_b.shape)

	WriteOriginal("original_red.csv",img_r)
	WriteOriginal("original_green.csv",img_g)
	WriteOriginal("original_blue.csv",img_b)

	print("File sizes of matrix RGB original: ")
	print(findsize("original_red.csv"))
	print(findsize("original_green.csv"))
	print(findsize("original_blue.csv"))

	img_b = compression(img_b)
	img_g = compression(img_g)
	img_r = compression(img_r)

	#print(img_r)
	print("File sizes of matrix RGB compressed: ")

	WriteToCSV(img_b,"blue.csv")
	WriteToCSV(img_g,"green.csv")
	WriteToCSV(img_r,"red.csv")

	print(findsize("red.csv"))
	print(findsize("green.csv"))
	print(findsize("blue.csv"))

	rgb = numpy.dstack((img_b,img_g,img_r))
	cv2.imwrite('coded_img.bmp',rgb)

	#cv2.imshow('encoded_img.bmp',rgb)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	#print(img_g)
	#print(img_b)
	#img = cv2.imread(Image_)
	#cv2.imshow('image_original' , img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	#ArrayImage = numpy.asmatrix(ArrayImage)
	#for i in ArrayImage:
		#print(i) 
	return ArrayImage

def toImage(ArrayImage):

	return img2


def checkDictionary(value,dictionary,dict_size): # if the dictionary value appears more than two times
	counter= 0
	for j in range(dict_size):
		if dictionary[str(j)] == value:
			counter = counter +1

	if counter < 2:
		return False
	else:
		return True
def updateDictionary(value, dictionary, dict_size):
	dictionary[str(dict_size-1)] = value

	return dictionary
def initializeResultMatrix(rows,cols ,ArrayImage):
	result = [[0] * rows] * cols
	result = ArrayImage
	return result

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



def updateResultMatrix(code_value,row_number ,cols , result):	
	for j in range(cols):
		result[row_number][j] = 0
	result[row_number][0] = code_value
	return result




 
def compression(ArrayImage):   #Applying Spatial redundancy LZW compression
	rows,cols = ArrayImage.shape
	flatArray = ArrayImage.flatten()
	dict_size = 256
	dictionary = {}
	for i in range(dict_size):
		dictionary[str(i)] = i
	#print(dictionary)

	ArrayImage = flatArray.reshape(rows,cols)
	#print(ArrayImage)

	result = [[0] * rows] * cols

	#(result)

	boolean = 0
	value = 0
	first = 0

	result = initializeResultMatrix(rows , cols , ArrayImage)
	for i in range(rows):
		first = ArrayImage[i][0]
		for j in range(cols):
			if first == ArrayImage[i][j]:
				boolean = 1
				value = ArrayImage[i][j]
			else:
				boolean = 0
				break


		if boolean == 1:
			#print(value) 
			#print("Is redundant added to dictionary from row number")
			#print(i)
			#print("The new short codewords is ")
			if checkDictionary(value, dictionary, dict_size):
				pass
			else:
				dict_size = dict_size +1
				dictionary = updateDictionary(value,dictionary,dict_size)
				
			result = updateResultMatrix(dictionary[str(dict_size-1)],i,cols , result)

	return result


def decompression(dictionary):
 	#dictionary.reshape(dictionary,rows,)
	ArrayImage = codewords

	return ArrayImage


Pic = toArray('GPS.bmp')
#Pic = toImage(ArrayImage)
#cv2.destroyAllWindows()
