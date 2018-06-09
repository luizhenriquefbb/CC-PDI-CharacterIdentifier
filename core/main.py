# python modules
import pickle

# my modules
import ImageToAscii
import Levenshtein
import util
import FixPerspective

# downloaded modules
import cv2

def identifyCharacter(image1_path):

	# read image
	image = cv2.imread(image1_path)


	# Use technology similar to QR code to correct image angulation
	warped = FixPerspective.fixPerspective(imageOpenCV=image)


	# Remove colored pixels to compare only black ones
	warped = util.cleanImage(warped)

	# resize image
	image = util.resizeImage(warped)

	# show the original and scanned images
	print("STEP 3: Apply perspective transform")
	cv2.imshow("Original", image)
	cv2.waitKey(0)

	# image to ascii art
	ascii1 = ImageToAscii.handle_image_conversion(image=image)
	print ("ascii da imagem de entrada")
	print ascii1


	# find most similar key
	# load KNN table
	filehandler = open("matrix-KNN.pickle", 'r')
	matrix = pickle.load(filehandler)

	smallerDistance = float('inf') # a very large number
	result = None
	for case in matrix:
		distance = Levenshtein.levenshtein(ascii1, case[0], signficance=case[1])
		if distance < smallerDistance:
			smallerDistance = distance
			result = case[1]
	

	print ("distance = " , smallerDistance)
	print ("result = " , result)

if __name__ == '__main__':
	import argparse
	
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=False,
					help="Path to the image to be scanned")
	args = vars(ap.parse_args())

	if args["image"] == None:
		image1 = "../testeCases/unknown/f.png"
		
	else:
		# load the image and compute the ratio of the old height
		# to the new height, clone it, and resize it
		image1 = args["image"]
	

	print("checking "+ image1 + " ...")


	identifyCharacter(image1)

