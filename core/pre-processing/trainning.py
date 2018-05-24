'''
Run trainning

go to core folder and run 'python pre-processing/trainning.py'
'''
import os
import sys
import pickle
sys.path.append("../core")
import ImageToAscii

def main():
	'''
	Steps:

	Read all images of "testeCases/" folder catalogging by their names
	i.e: image A.png contain the best case of an "A" char, so save it into the KNN

	KNN will be a ordered matrix nX2
		n == number of tests char
		2 = ascii art + corresponding char

	Do not read from "testeCases/unknown/". This images will be use to test the KNN
	'''

	# Read all images of "testeCases/" folder catalogging by their names
	folder = "../testeCases"

	paths = [os.path.join(folder, nome) for nome in os.listdir(folder)]
	files = [arq for arq in paths if os.path.isfile(arq)]
	pngs = [arq for arq in files if arq.lower().endswith(".png")]

	
	# convert each image to ascii and store into matrix
	matrix = []
	for imagePath in pngs:
		asciiImage = ImageToAscii.handle_image_conversion(imagePath)
		imageName = imagePath.replace(folder+'/', '').replace('.png','')
		matrix.append([asciiImage, imageName])

	
	# save matrix
	filehandler = open("matrix-KNN.pickle", 'w')
	pickle.dump(matrix, filehandler)

if __name__ == '__main__':
	main()
