'''
Run trainning

IMPORTANT:
YOU MUST BE IN core folder and run 'python pre-processing/trainning.py'
'''
# default libs
import os
import sys
import pickle

# imported libs
import cv2

# my libs
sys.path.append("../core")
import ImageToAscii
import util

def main():
	'''
	Steps:

	Read all images of "testeCases/" folder catalogging by their names
	i.g: image A.png contain the best case of an "A" char, so save it into the KNN

	KNN will be a ordered matrix nX2
		n == number of tests char
		2 = ascii art + corresponding char

	Do not read from "testeCases/unknown/". This images will be use to test the KNN
	'''

	# Get all image paths
	folder = "../testeCases"

	paths = [os.path.join(folder, nome) for nome in os.listdir(folder)]
	files = [arq for arq in paths if os.path.isfile(arq)]
	pngs = [arq for arq in files if arq.lower().endswith(".png")]

	
	# convert each image to ascii and store into matrix
	matrix = []
	for imagePath in pngs:

		# read image
		image = cv2.imread(imagePath)

		# resize image to compare always image of same sizes
		image = util.resizeImage(image)

		# Convert to ascii and build matrix
		asciiImage = ImageToAscii.handle_image_conversion(image=image)
		imageName = imagePath.replace(folder+'/', '').replace('.png', '')
		matrix.append([asciiImage, imageName])

	
	# save matrix
	filehandler = open("matrix-KNN.pickle", 'w')
	pickle.dump(matrix, filehandler)

if __name__ == '__main__':
	main()
