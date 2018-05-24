import logging
import ImageToAscii
import Levenshtein

def main(image1_path, image2_path):

	# read image
	
	# Use technology similar to QR code to correct image angulation

	# resize image


	# image to ascii art
	ascii1 = ImageToAscii.handle_image_conversion(image1_path)
	ascii2 = ImageToAscii.handle_image_conversion(image2_path)


	# find most similar key
	distance = Levenshtein.levenshtein(ascii1, ascii2)

	print distance

if __name__ == '__main__':
	import sys

	# pass path by terminal
	# image1 = sys.argv[1]
	# image2 = sys.argv[2]

	# 
	image1 = "testeCases/A-1.png"
	image2 = "testeCases/A.png"
	
	main(image1, image2)
