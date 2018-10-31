#Date 31 October 2018
#Author Siyabonga Magubane
#references http://www.codecodex.com/wiki/ , http://www.codecodex.com/wiki/LZW , https://github.com/code-blooded/Image-Compression/blob/master/median-cut-algorithm/main.py


import cv2
import numpy 
import collections
import os
import csv
import re
from helpers import *

from PIL import Image

class LZW_compression:

    # Initializer / Instance Attributes
	def __init__(self):
		self.dictionary = {}
		self.dict_size = 255


	 
	
	def checkDictionary(self,value,dictionary,dict_size): # if the dictionary value appears more than two times
		counter= 0
		for j in range(dict_size):
			if dictionary[str(j)] == value:
				counter = counter +1

		if counter < 2:
			return False
		else:
			return True
	def initializeResultMatrix(self,rows,cols ,ArrayImage):
		result = [[0] * rows] * cols
		result = ArrayImage
		return result

	def updateDictionary(self,value, dictionary, dict_size):
		dictionary[str(dict_size-1)] = value

		return dictionary

	def updateCompressionMatrixRow(self,dictionary,dict_size,row_number ,cols , result):
		code_value = dictionary[str(dict_size-1)]	
		for j in range(cols):
			result[row_number][j] = 0
		result[row_number][0] = code_value
		return result

	def updateDecompressionMatrixRow(self,dictionary,dict_size,row_number ,cols , result):
		code_value = dictionary[str(dict_size-1)]	
		for j in range(cols):
			result[row_number][j] = code_value
		return result

	def initializeDictionary(self):

		for i in range(self.dict_size):
			self.dictionary[str(i)] = i

		return self.dictionary
	def compression(self,ArrayImage):   #Applying Spatial redundancy LZW compression
		rows,cols = ArrayImage.shape
		self.dictionary = self.initializeDictionary()

		result = [[0] * rows] * cols

		#(result)

		boolean = 0
		value = 0
		first = 0

		result = self.initializeResultMatrix(rows , cols , ArrayImage)
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
				if self.checkDictionary(value, self.dictionary, self.dict_size):
					pass
				else:
					self.dict_size = self.dict_size +1
					self.dictionary = self.updateDictionary(value,self.dictionary,self.dict_size)
					
				result = self.updateCompressionMatrixRow(self.dictionary,self.dict_size,i,cols , result)

		return result
	 

	def decompression(self,ArrayImage): #decompression of LZW compression algorithm
	 	rows , cols = ArrayImage.shape
	 	result = self.initializeResultMatrix(rows , cols , ArrayImage)
	 	for j in range(rows):
	 		if isCompressRow(result,j,cols):
	 			result = self.updateDecompressionMatrixRow(self.dictionary,self.dict_size, j , cols , result)
	 		else:
	 			pass
	 	
	 	return result




 



