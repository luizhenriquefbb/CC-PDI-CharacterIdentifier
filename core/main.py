import pickle
import ImageToAscii
import Levenshtein
import util

import cv2

def identifyCharacter(image1_path):

	# read image
	image = cv2.imread(image1_path)


	# Use technology similar to QR code to correct image angulation
	# TODO:



	# resize image
	image = util.resizeImage(image, 67,67)


	# image to ascii art
	ascii1 = ImageToAscii.handle_image_conversion(image_filepath=image1_path)


	# find most similar key
	# load KNN table
	filehandler = open("matrix-KNN.pickle", 'r')
	matrix = pickle.load(filehandler)

	smallerDistance = float('inf') # a very large number
	result = None
	for case in matrix:
		distance = Levenshtein.levenshtein(ascii1, case[0])
		if distance < smallerDistance:
			smallerDistance = distance
			result = case[1]
	

	print ("distance = " , smallerDistance)
	print ("result = " , result)

if __name__ == '__main__':
	import sys

	# pass path by terminal
	# image1 = sys.argv[1]
	
	image1 = "../testeCases/unknown/teste1.png"

	print("checking "+ image1 + " ...")


	identifyCharacter(image1)
