import pickle
import ImageToAscii
import Levenshtein

def main(image1_path):

	# read image
	
	# Use technology similar to QR code to correct image angulation

	# resize image


	# image to ascii art
	ascii1 = ImageToAscii.handle_image_conversion(image1_path)


	# find most similar key
	# load KNN table
	filehandler = open("matrix-KNN.pickle", 'r')
	matrix = pickle.load(filehandler)

	# TODO: validate matrix

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


	main(image1)
